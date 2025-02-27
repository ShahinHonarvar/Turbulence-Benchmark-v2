from itertools import islice, cycle

def circular_list_slice(circular_list, start, end):
    return [circular_list[i % len(circular_list)] for i in range(start, end)]

def lists_with_product_equal_n(circular_list):

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    n = 85
    circular_list = list(circular_list)
    sublists = []
    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) - i + 1):
            sublist = circular_list_slice(circular_list, i, i + j)
            if product(sublist) == n:
                sublists.append(sublist)
    return sublists