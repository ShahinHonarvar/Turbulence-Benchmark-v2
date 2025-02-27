from itertools import combinations_with_replacement

def lists_with_product_equal_n(lst):
    product = 632
    result = []
    for r in range(len(lst)):
        for comb in combinations_with_replacement(lst, r):
            if product // comb[-1] in comb[:-1] and product % comb[-1] == 0:
                comb = sorted(comb)
                if comb not in result:
                    result.append(comb)
    return result