def lists_with_product_equal_n(circular_list):
    """
  Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle. The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals 15. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
  """

    def get_sublists(circular_list):
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list) + 1):
                sublist = circular_list[i:j]
                if len(sublist) > 1 and sublist[-1] * sublist[0] == 15:
                    sublists.append(sublist)
        return sublists

    def is_circular(circular_list):
        return circular_list[0] * circular_list[-1] == 15
    if is_circular(circular_list):
        return get_sublists(circular_list)
    else:
        return []