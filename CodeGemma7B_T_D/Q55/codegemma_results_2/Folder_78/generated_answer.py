from itertools import cycle

def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals 74.
    """
    result = []
    current_list = []
    product = 1
    for i in cycle(circular_list):
        current_list.append(i)
        product *= i
        while product > 74 or (product == 74 and len(current_list) > len(circular_list)):
            product //= current_list.pop(0)
        if product == 74 and len(current_list) <= len(circular_list):
            result.append(current_list[:])
    return result