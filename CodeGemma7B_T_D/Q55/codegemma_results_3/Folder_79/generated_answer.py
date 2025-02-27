from itertools import islice

def lists_with_product_equal_n(list):
    """
    Takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -83.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    for i in range(len(list)):
        for j in range(i + 1, len(list) + 1):
            sublist = list[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == -83:
                yield sublist