from functools import reduce

def lists_with_product_equal_n(circular_list):

    def is_valid_sublist(sublist):
        product = reduce(lambda x, y: x * y, sublist)
        return product == 5

    def circular_sublists(sublist):
        length = len(sublist)
        return [sublist[i:i + length] for i in range(length)] + [sublist]

    def sublists_with_product(sublists):
        return [sublist for sublist in sublists if is_valid_sublist(sublist)]
    sublists = [circular_list[i:j] for i in range(len(circular_list)) for j in range(i + 1, len(circular_list) + 1)]
    circular_sublists_all = [circular_sublists(sublist) for sublist in sublists]
    valid_sublists = sublists_with_product(reduce(lambda x, y: x + y, circular_sublists_all))
    return valid_sublists