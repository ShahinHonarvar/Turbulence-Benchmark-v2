from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product(sublist):
        total = 1
        for num in sublist:
            total *= num
        return total
    sublists = []
    for length in range(1, len(circular_list) + 1):
        for sublist in combinations(circular_list, length):
            if product(sublist) == 15:
                sublists.append(list(sublist))
    return sublists