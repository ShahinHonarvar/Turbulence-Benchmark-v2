def lists_with_product_equal_n(circular_list):
    """
    This function returns a list of sublists, each of which contains the contiguous integers from the given list 
    such that their product equals -81. Each sublist in the returned list can be of any size as long as it is smaller 
    than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If 
    there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists 
    in the returned list does not matter.
    The function takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent 
    to each other to form a circle.
    """
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list) + i + 1):
            k = j % len(circular_list)
            product *= circular_list[k]
            sublist.append(circular_list[k])
            if product == -81:
                sublists.append(sublist[:])
            elif product > -81:
                break
    return sublists