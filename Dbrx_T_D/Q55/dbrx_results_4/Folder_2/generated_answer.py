from itertools import islice

def sub_lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sub_lst = lst[i:j + 1]
            if product(sub_lst) == n:
                result.append(sub_lst)
    return result

def circular_shifts(lst):
    return [lst[i:] + lst[:i] for i in range(len(lst))]

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n):
    if n == 0:
        return [[0]] if 0 in lst else []
    shifts = circular_shifts(lst)
    return [sub for sub in sub_lists_with_product_equal_n(lst, n) if sub not in sub_lists_with_product_equal_n(lst[:-1], n) and sub not in sub_lists_with_product_equal_n(lst[1:], n)] + [sub for sub in sum([sub_lists_with_product_equal_n(shift, n) for shift in shifts], []) if sub not in sub_lists_with_product_equal_n(lst, n)]