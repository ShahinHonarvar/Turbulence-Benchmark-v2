import itertools

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for r in range(1, n + 1):
            for sub_lst in itertools.combinations(lst[i:] + lst[:i], r):
                if sub_lst and eval('*'.join(map(str, sub_lst))) == -30:
                    result.append(list(sub_lst))
    return result