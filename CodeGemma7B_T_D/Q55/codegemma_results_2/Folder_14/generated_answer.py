def lists_with_product_equal_n(lst):
    """Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers.
  In a circular list, the head and the tail are adjacent to each other to form a circle.
  The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -72.
  Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
  If no such sublist exists, the function should return an empty list.
  If there are duplicates of such a sublist, they should all be contained in the returned list.
  The order of sublists in the returned list does not matter."""
    sublists = []
    for i in range(len(lst)):
        product = lst[i]
        sublist = [lst[i]]
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == -72:
                sublists.append(sublist[:])
            elif product > -72:
                break
        if product == -72:
            sublists.append(sublist[:])
    return sublists