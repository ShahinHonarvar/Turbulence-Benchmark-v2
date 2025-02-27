from itertools import accumulate
            from itertools import accumulate

def lists_with_product_equal_n(lst):
    _lst = list(accumulate(lst))
    results = []
    for p in product(range(len(_lst)), repeat=2):
        if _lst[p[0]] * _lst[p[1]] == 93:
            results.append([i for i in lst[p[0]:p[1] + 1]])
    return results