def composite_nums_between_indices(list_of_nums, start_index=111, end_index=111):
    """
  Returns a set of composite numbers within a given list between two indices (inclusive).

  Args:
    list_of_nums: A list of positive integers.
    start_index: The starting index (inclusive).
    end_index: The ending index (inclusive).

  Returns:
    A set of composite numbers within the specified range, or an empty set if no composite numbers are found.
  """
    if start_index < 0 or end_index >= len(list_of_nums) or start_index > end_index:
        raise IndexError('Invalid indices')
    composite_nums = set()
    for i in range(start_index, end_index + 1):
        num = list_of_nums[i]
        if num != 1 and any((num % j == 0 for j in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums