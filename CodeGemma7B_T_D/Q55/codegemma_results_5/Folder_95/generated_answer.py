from itertools import combinations_with_replacement

def lists_with_product_equal_n(circular_list):
    circular_list *= 2
    for list_size in range(len(circular_list)):
        for sublist in combinations_with_replacement(circular_list, list_size):
            if len(set(sublist)) == len(sublist) and all((number % 2 == 0 for number in sublist)):
                if reduce(lambda x, y: x * y, sublist) == 28:
                    return sorted(list(sublist))
    return []