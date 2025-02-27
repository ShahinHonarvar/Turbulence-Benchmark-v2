from itertools import permutations
    from itertools import permutations

def lists_with_product_equal_n(circular_list):

    def find_sublists(circular_list, product):
        return [[circular_list[i + j] for j in range(len(circular_list))] for i in range(len(circular_list)) if product in [i * j for i, j in permutations(circular_list[i:], 2)]]
    return [sublist for sublist in find_sublists(circular_list, 47) if len(sublist) <= len(circular_list)]