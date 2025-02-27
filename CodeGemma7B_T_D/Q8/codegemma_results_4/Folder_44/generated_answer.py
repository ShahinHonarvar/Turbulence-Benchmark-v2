def all_even_ints_exclusive(nums):
    """
  #    This function returns a list of even numbers from index 81 to 86 (exclusive) starting from the initial list.
  #    Returns an empty list if no even numbers are present in the specified range.
  """
    if not nums:
        return []
    min_value = float('inf')
    max_value = float('-inf')
    for num in nums:
        if num % 2 == 0 and num >= min_value + 2 and (num < max_value - 2):
            max_value = num
        elif num % 2 == 0 and num > min_value + 2:
            min_value = num
        elif num % 2 == 0 and num < max_value - 2:
            max_value = num
        elif num % 2 == 0 and num <= max_value - 2 and (num > min_value + 2):
            min_value = num
        elif num % 2 == 0 and num == min_value:
            min_value = num - 1
            break
        elif num % 2 == 0 and num == max_value:
            max_value = num + 1
            break
    if min_value == float('inf'):
        return []
    result = []
    for num in nums:
        if num % 2 == 0 and num >= min_value and (num < max_value):
            result.append(num)
    return result