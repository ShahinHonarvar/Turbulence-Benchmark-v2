def lists_with_product_equal_n(circular_list):
    """
    Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle. The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals 28. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
    """

    def product(sublist):
        """Calculates the product of integers in a sublist."""
        result = 1
        for num in sublist:
            result *= num
        return result

    def find_sublists(index):
        """Recursively finds sublists with product equal to 28 starting at the given index."""
        result = []
        for size in range(1, len(circular_list) + 1):
            sublist = circular_list[index:index + size]
            if product(sublist) == 28:
                result.append(sublist)
        for next_index in range(index + 1, len(circular_list)):
            sublists = find_sublists(next_index)
            for sublist in sublists:
                if product([circular_list[index]] + sublist) == 28:
                    result.append([circular_list[index]] + sublist)
        return result
    return find_sublists(0)