from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    """
  Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers.
  In a circular list, the head and the tail are adjacent to each other to form a circle.
  The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -97.
  Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
  If no such sublist exists, the function should return an empty list.
  If there are duplicates of such a sublist, they should all be contained in the returned list.
  The order of sublists in the returned list does not matter.
  """
    product = -97
    sublists = []
    for i in range(len(circular_list)):
        current_product = 1
        current_sublist = []
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]
            current_sublist.append(circular_list[j])
            if current_product == product:
                sublists.append(current_sublist)
            if current_product > product:
                break
    return sublists