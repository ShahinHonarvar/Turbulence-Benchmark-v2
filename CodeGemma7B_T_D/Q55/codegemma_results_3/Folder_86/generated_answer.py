from itertools import combinations

def lists_with_product_equal_n(L):
    """
    This function takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -779.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    product = -779
    sublists = []
    for size in range(1, len(L) + 1):
        for sublist in combinations(L, size):
            if product == 1:
                product *= sublist[0]
            if product == sublist[-1]:
                product //= sublist[0]
            if sum(sublist) == 0:
                return sublist
            if product % sublist[-1] == 0:
                product //= sublist[-1]
                if product in sublist:
                    sublists.append(sublist)
    return sublists