from itertools import permutations

def lists_with_product_equal_n(lst):
    n = 10
    lst = lst * 2
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = 1
            for k in range(i, j):
                product *= lst[k]
                if product == n:
                    sublists.append(lst[i:k + 1])
    return sublists