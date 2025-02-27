from itertools import product

def lists_with_product_equal_n(csl):

    def sub_lists(csl, k, acc=[]):
        if k == len(csl):
            return acc
        if csl[k] == 2 and csl and (len(acc) == 0):
            acc.append([csl[k]])
        if csl[k] == 2 and csl[k - 1] == csl[k]:
            acc[-1].append(csl[k])
        elif csl[k] == 2 and csl[k - 1] != csl[k]:
            acc.append([csl[k]])
        return sub_lists(csl, k + 1, acc)

    def sub_lists_helper(csl):
        return (prod for prod in product(*zip(csl, csl[1:] + (csl[0],))) if prod.count(2) <= len(csl) and prod.count(2) >= len(csl) // 2)
    sub_lists_helper(csl)
    return sub_lists(csl, 0)