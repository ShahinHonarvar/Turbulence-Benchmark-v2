def lists_with_product_equal_n(nums):
    """
  Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle. The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -6. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
  """
    results = []
    current_list = []
    current_product = 1
    for num in nums + nums:
        current_product *= num
        current_list.append(num)
        while current_product > -6:
            current_product //= current_list.pop(0)
        if current_product == -6:
            results.append(current_list[:])
    return results