def lists_with_product_equal_n(circular_list):
    """
    This function takes a circular list of integers and returns a list of sublists
    each of which contains the contiguous integers from the given list such that their
    product equals 6. Each sublist in the returned list can be of any size as
    long as it is smaller than or equal to the size of the given list. If no such
    sublist exists, the function should return an empty list. If there are
    duplicates of such a sublist, they should all be contained in the returned
    list. The order of sublists in the returned list does not matter.
    """

    def is_circular(lst):
        return lst[0] * lst[-1] == lst[-2] * lst[1]

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                sublist = lst[i:j + 1]
                if is_circular(sublist):
                    sublists.append(sublist)
        return sublists

    def has_sublist_with_product_equal_n(lst):
        for sublist in get_sublists(lst):
            if sublist and sublist[0] * sublist[-1] == sublist[-2] * sublist[1]:
                return True
        return False
    if not has_sublist_with_product_equal_n(circular_list):
        return []
    return get_sublists(circular_list)