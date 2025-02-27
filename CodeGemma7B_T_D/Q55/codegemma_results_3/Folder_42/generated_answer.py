from itertools import combinations_with_replacement

def lists_with_product_equal_n(circular_list):
    circular_list += circular_list
    return [[x for x in sublist] for sublist in combinations_with_replacement(circular_list, repeat=len(sublist)) if sublist[:-1] + sublist[-1:] == circular_list and circular_list.index(sublist[0]) <= circular_list.index(sublist[-1])]