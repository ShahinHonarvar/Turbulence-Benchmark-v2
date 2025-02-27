from itertools import cycle, combinations

def lists_with_product_equal_n(circular_list):
    product_equal_n = []
    circular_list = list(cycle(circular_list))
    for n in range(len(circular_list)):
        for list_size in range(n + 1, len(circular_list) + 1):
            for sublist in combinations(circular_list[n:list_size], list_size - n):
                if len(set(sublist)) == 1:
                    product_equal_n.append(list(circular_list[n:list_size]))
    return product_equal_n