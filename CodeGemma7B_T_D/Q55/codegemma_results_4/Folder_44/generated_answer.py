def lists_with_product_equal_n(list_of_nums):
    """
  Returns a list of sublists each of which contains the contiguous integers from the
  given list such that their product equals 29.

  Args:
    list_of_nums: A circular list of integers.

  Returns:
    A list of sublists or an empty list if no such sublist exists.
  """
    list_of_nums_continuously = list_of_nums + list_of_nums + list_of_nums
    groups_of_contiguous_nums = []
    current_group = []
    current_product = 1
    for num in list_of_nums_continuously:
        current_group.append(num)
        current_product *= num
        if current_product == 29:
            groups_of_contiguous_nums.append(current_group[:])
            current_product = 1
            current_group = []
        elif current_product > 29:
            current_product = 1
            current_group = []
    return groups_of_contiguous_nums