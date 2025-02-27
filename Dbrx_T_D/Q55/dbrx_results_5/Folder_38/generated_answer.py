from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -23
    result = []
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if sublists_with_product_equal_n(comb):
                result.append(list(comb))
    return result