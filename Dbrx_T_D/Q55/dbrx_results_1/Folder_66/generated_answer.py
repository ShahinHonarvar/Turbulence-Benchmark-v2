from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist):
        for i in range(1, len(sublist) + 1):
            for comb in combinations(sublist, i):
                if sublst_product(comb) == 78:
                    return [list(comb)]
        return []

    def sublst_product(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    return [sl for i in range(1, len(circular_list) + 1) for j in combinations(circular_list, i) for sl in sublists_with_product_equal_n(j)]