def lists_with_product_equal_n(given_list):
    """
    Given a circular list of integers, return a list of sublists such that their product equals -9.
    Each sublist can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """

    def helper(product, start_index):
        """
        Helper function to find sublists with product equal to -9.
        """
        if product == -9 and helper_list[-1] - helper_list[0] + 1 <= len(given_list):
            result.append(helper_list[:])
        if start_index + 1 >= len(given_list):
            return
        helper_list.append(given_list[start_index + 1])
        product *= given_list[start_index + 1]
        helper(product, start_index + 1)
        helper_list.pop()
        product //= given_list[start_index + 1]
    helper_list = [given_list[0]]
    result = []
    helper(-9, 0)
    return result