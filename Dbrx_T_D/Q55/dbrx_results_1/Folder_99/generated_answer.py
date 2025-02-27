from itertools import islice

def sublists_with_product_equal_n(lst, n):
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst) - size + 1):
            sublist = lst[i:i + size]
            product = 1
            for j in sublist:
                product *= j
                if product > n:
                    break
                if product == n:
                    result.append(sublist)
    return result

def circular_list(lst):
    return [lst[-1]] + lst[:-1]