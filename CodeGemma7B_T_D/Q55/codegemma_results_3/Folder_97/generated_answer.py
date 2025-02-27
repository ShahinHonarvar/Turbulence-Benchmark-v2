def lists_with_product_equal_n(circular_list):
    """
    Given an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains contiguous integers from the given list such that their product equals -938. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
    """
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            if product * circular_list[j] == -938:
                sublists.append(circular_list[i:j + 1])
            product *= circular_list[(j + 1) % len(circular_list)]
        if product == -938:
            sublists.append(circular_list[i:])
    return sublists