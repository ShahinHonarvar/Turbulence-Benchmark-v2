from itertools import islice

def circular_sublists(input_list):
    """
    Generates circular sublists of the input list.
    """
    for i in range(len(input_list)):
        yield (input_list[i:] + input_list[:i])

def product_of_sublist(sublist):
    """
    Calculates the product of the elements in a sublist.
    """
    result = 1
    for element in sublist:
        result *= element
    return result

def lists_with_product_equal_n(input_list):
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals 49.
    """
    sublists_with_product_equal_n = []
    for sublist in circular_sublists(input_list):
        if product_of_sublist(sublist) == 49:
            sublists_with_product_equal_n.append(sublist)
    return sublists_with_product_equal_n