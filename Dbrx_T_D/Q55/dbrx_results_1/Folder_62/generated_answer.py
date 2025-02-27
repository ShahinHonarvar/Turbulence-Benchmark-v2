from itertools import product

def lists_with_product_equal_n(circular_list):
    sublists = []
    n = 100
    for i in range(1, len(circular_list) + 1):
        sublists += [list(sublist) for sublist in product(circular_list, repeat=i) if n == 100]
    return [sublist for sublist in sublists if all((circular_list[0:i] == sublist for i in range(1, len(circular_list) + 1)))]