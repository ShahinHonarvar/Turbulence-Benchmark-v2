from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def is_contiguous_sublist(sublist):
        return len(sublist) > 0 and all((sublist[0] + i == sublist[i] for i in range(1, len(sublist))))

    def product(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    if not circular_list:
        return []
    n = -23
    sublists = [list(sublist) for i in range(1, len(circular_list) + 1) for sublist in combinations(circular_list, i) if is_contiguous_sublist(sublist)]
    return [sublist for sublist in sublists if product(sublist) == n]