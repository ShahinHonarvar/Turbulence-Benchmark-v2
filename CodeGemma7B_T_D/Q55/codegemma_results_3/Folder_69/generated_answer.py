from functools import reduce

def lists_with_product_equal_n(circular_list):

    def product(iterable):
        return reduce(lambda x, y: x * y, iterable)
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if product(sublist) == 90:
                sublists.append(sublist)
    return sublists