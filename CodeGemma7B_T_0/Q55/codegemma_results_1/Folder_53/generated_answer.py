def lists_with_product_equal_n(circ):
    """
    This function takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -87.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """

    def product(sublist):
        """
        This function calculates the product of the elements in a sublist.
        """
        product = 1
        for element in sublist:
            product *= element
        return product

    def find_sublists(circ, product):
        """
        This function finds all sublists in a circular list that have a product equal to the given product.
        """
        sublists = []
        for i in range(len(circ)):
            for j in range(i + 1, len(circ) + 1):
                sublist = circ[i:j]
                if product(sublist) == product:
                    sublists.append(sublist)
        return sublists
    if product(circ) == -87:
        return find_sublists(circ, -87)
    else:
        return []