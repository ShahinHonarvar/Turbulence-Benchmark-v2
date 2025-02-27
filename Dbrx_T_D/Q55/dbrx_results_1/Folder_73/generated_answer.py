from itertools import combinations

def lists_with_product_equal_n(lst):

    def circular_product(sublist):
        if not sublist:
            return 1
        else:
            return circular_product(sublist[1:]) * sublist[0]
    result = []
    for i in range(1, len(lst) + 1):
        for comb in combinations(lst, i):
            if circular_product(comb) == 40:
                result.append(list(comb))
    return result