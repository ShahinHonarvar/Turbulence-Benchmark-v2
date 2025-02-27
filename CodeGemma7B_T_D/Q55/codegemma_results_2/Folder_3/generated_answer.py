from itertools import islice

def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for integer in sublist:
            product *= integer
        return product
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = list(islice(circular_list, i, j + 1))
            sublists.append(sublist)
    result = []
    for sublist in sublists:
        if product_of_sublist(sublist) == -22:
            result.append(sublist)
    return result