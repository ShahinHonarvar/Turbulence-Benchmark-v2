from itertools import combinations

def lists_with_product_equal_n(lst):
    circ_lst = lst + lst
    n = 13
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst)):
            prod = 1
            for k in circ_lst[i:j + 1]:
                prod *= k
                if prod == n:
                    res.append(circ_lst[i:j + 1])
    return res