from itertools import accumulate

def lists_with_product_equal_n(num_list):
    """
    This function takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -76.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    product = -76
    sublists = []
    for i in range(len(num_list)):
        temp_cumprod = list(accumulate(num_list[i:] + num_list[:i], initial=num_list[i]))
        sublists.extend([num_list[i:i + n] for n in range(1, len(temp_cumprod) + 1) if temp_cumprod[n - 1] == product])
    return sublists