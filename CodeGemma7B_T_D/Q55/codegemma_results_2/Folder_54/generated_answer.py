from functools import reduce

def lists_with_product_equal_n(circular_list):
    return [[i for i in circular_list[circular_list.index(n):]] for n in circular_list if reduce(lambda x, y: x * y, circular_list[circular_list.index(n):]) == -17]