def lists_with_product_equal_n(circular_list):
    """
    Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle. The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -93. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
    """
    products = {}
    current_product = 1
    sublists = []
    i = 0
    for element in circular_list + circular_list:
        current_product *= element
        while current_product > -93 or element == 0:
            current_product /= circular_list[i]
            i += 1
        if current_product in products:
            for sublist in products[current_product]:
                sublists.append(sublist + [element])
        else:
            products[current_product] = [circular_list[i:]]
    return sublists