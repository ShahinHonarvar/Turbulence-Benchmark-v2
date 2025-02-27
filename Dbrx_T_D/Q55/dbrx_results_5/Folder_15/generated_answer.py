from itertools import islice

def circular_list(lst):
    return lst[-1:] + lst[:-1]

def consecutive_product(lst, n):
    result = []
    for i in range(len(lst)):
        sub_list = []
        product = 1
        for j in range(i, len(lst)):
            sub_list.append(lst[j])
            product *= lst[j]
            if product == n:
                result.append(sub_list[:])
            elif product > n:
                break
    return result

def lists_with_product_equal_n(lst, n):
    return [sub_list for sub_list in [consecutive_product(circular_list(lst[:i] + lst[i + 1:]), n) for i in range(len(lst))] if sub_list]