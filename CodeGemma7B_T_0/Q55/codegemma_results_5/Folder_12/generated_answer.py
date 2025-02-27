def lists_with_product_equal_n(circular_list):
    """
  Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle. The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -18. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
  """

    def get_sublists(circular_list, start, end):
        sublist = []
        for i in range(start, end + 1):
            sublist.append(circular_list[i])
        return sublist

    def get_product(circular_list, start, end):
        product = 1
        for i in range(start, end + 1):
            product *= circular_list[i]
        return product

    def find_sublists(circular_list, start, end):
        if start == end:
            return []
        if get_product(circular_list, start, end) == -18:
            return [get_sublists(circular_list, start, end)]
        sublists = []
        for i in range(start + 1, end + 1):
            sublists.extend(find_sublists(circular_list, i, end))
        for i in range(start + 1, end):
            sublists.extend(find_sublists(circular_list, start, i))
        return sublists
    return find_sublists(circular_list, 0, len(circular_list) - 1)