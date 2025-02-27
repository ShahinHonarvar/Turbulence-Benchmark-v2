from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    return [sublist for length in range(1, len(circular_list) + 1) for sublist in combinations(circular_list, length) if product(sublist) == 6]