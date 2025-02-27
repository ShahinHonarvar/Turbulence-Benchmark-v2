from itertools import combinations

def lists_with_product_equal_n(circular_list):
    product = -968

    def product_of_list(sublist):
        return product(list(sublist))

    def is_circular_sublist(circular, sublist):
        for index in range(len(circular)):
            window = circular[index:index + len(sublist)]
            if product_of_list(window) == product:
                return True
        return False
    size = len(circular_list)
    if size == 0:
        return []
    sublists = [list(c) for c in combinations(circular_list, size)]
    circular_sublists = [sublist for sublist in sublists if is_circular_sublist(circular_list, sublist)]
    return circular_sublists