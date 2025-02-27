from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-10):
    result = []
    for i in range(len(lst)):
        sub_prod = 1
        for j in range(i, len(lst)):
            sub_prod *= lst[j]
            if sub_prod == n:
                result.append(lst[i:j + 1])
                break
            elif sub_prod < n:
                break
    return result

def circular_lists_with_product_equal_n(lst, n=-10):
    circular_list = cycle(lst)
    return [sublist for sublist in itertools.product(circular_list, repeat=len(lst)) if reduce(lambda x, y: x * y, sublist) == n]