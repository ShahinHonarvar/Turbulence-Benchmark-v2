from itertools import product

def lists_with_product_equal_n(circular_list):
    return [sublist for p in product(circular_list, repeat=len(circular_list)) if sum(p) == 25 for sublist in split_list_at_an_index(circular_list, p)]

def split_list_at_an_index(circular_list, p):
    for i in range(len(circular_list)):
        yield [circular_list[j] for j in range(i, len(circular_list)) + range(i)]