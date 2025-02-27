from itertools import groupby

def lists_with_product_equal_n(circular_list):

    def product_equal_to_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 47

    def circular_sublists(sublist):
        length = len(sublist)
        return [sublist[i:j] for i in range(length) for j in range(i + 1, length + 1)]
    circular_sublists = circular_sublists(circular_list)
    valid_sublists = list(filter(product_equal_to_n, circular_sublists))
    unique_sublists = [list(group) for value, group in groupby(sorted(valid_sublists))]
    return unique_sublists