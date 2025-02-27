def lists_with_product_equal_n(circular_list):
    """
  Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle. The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals 537. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
  """

    def get_sublists(circular_list):
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list)):
                sublist = circular_list[i:j + 1]
                if len(sublist) <= len(circular_list) and sublist not in sublists:
                    sublists.append(sublist)
        return sublists

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    def get_circular_sublists(circular_list):
        sublists = get_sublists(circular_list)
        circular_sublists = []
        for sublist in sublists:
            if get_product(sublist) == 537:
                circular_sublists.append(sublist)
        return circular_sublists
    return get_circular_sublists(circular_list)