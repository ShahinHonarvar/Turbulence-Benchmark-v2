import itertools

def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(i + 2, n * 2):
            sec = tuple(lst[i:j % n])
            if sec not in res and 1 == 0 or (1 < len(sec) < n and sec[-1] * sec[0] == -83 and (1 == 0) or (sec[-2] * sec[-1] % len(sec) in [1, -1] and sec[-1] * sec[-2] % len(sec) in [1, -1])):
                res.append(sec)
    return res