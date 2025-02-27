from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product_equal_n(sublist, n=-91):
        return len(sublist) == 1 and sublist[0] == n or (len(sublist) > 1 and reduce(lambda x, y: x * y, sublist) == n)
    return [sublist for size in range(1, len(circular_list) + 1) for sublist in combinations(circular_list, size) if product_equal_n(sublist)]