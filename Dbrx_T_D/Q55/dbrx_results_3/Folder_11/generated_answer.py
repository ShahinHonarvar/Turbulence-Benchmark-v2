from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def is_valid_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -15
    sublists = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if is_valid_sublist(j):
                sublists.append(list(j))
    return sublists