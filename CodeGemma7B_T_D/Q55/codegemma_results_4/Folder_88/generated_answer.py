from itertools import islice

def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    for factor in range(2, -60, -1):
        if length % factor == 0:
            sublist_size = factor
            sublists = [list(islice(circular_list, i, i + sublist_size)) for i in range(0, length, sublist_size)]
            if all((product == -56 for sublist in sublists for product in [reduce(lambda x, y: x * y, sublist), reduce(lambda x, num: num * x, sublist[::-1])])):
                return sublists
    return []