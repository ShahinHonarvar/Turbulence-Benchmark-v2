from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def valid_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product > 6:
                return False
            elif product == 6:
                return True
        return False
    sublists = []
    for sublist_length in range(1, len(circular_list) + 1):
        sublists.extend(combinations(circular_list, sublist_length))
    valid_sublists = [sublist for sublist in sublists if valid_sublist(sublist)]
    return valid_sublists