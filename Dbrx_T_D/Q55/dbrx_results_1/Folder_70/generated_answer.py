from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def has_product_equal_n(sublist, n=32):
        product = 1
        for num in sublist:
            product *= num
            if product > n:
                return False
            elif product == n:
                return True
        return False
    sublists = []
    for i in range(1, len(circular_list) + 1):
        sublists.extend(combinations(circular_list, i))
    return [sublist for sublist in sublists if has_product_equal_n(sublist)]