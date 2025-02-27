from itertools import islice, product

def lists_with_product_equal_n(circular_list):

    def adjacent_product(circular_list):
        for i in range(len(circular_list)):
            product_list = [circular_list[i], circular_list[(i + 1) % len(circular_list)]]
            yield product_list
    n = -61
    results = []
    for i in range(len(circular_list)):
        for sublist_size in range(1, len(circular_list)):
            sublist_generator = islice(adjacent_product(circular_list), i, i + sublist_size)
            product_result = product(*sublist_generator)
            if product_result == (n,):
                results.append(list(sublist_generator))
    return results