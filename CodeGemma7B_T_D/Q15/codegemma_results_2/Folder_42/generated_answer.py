def sum_odd_ints_inclusive(num_list):
    """Sums odd integers from index 29 to index 79, inclusive.

  Args:
    num_list: A list of integers.

  Returns:
    The sum of odd integers from index 29 to index 79, inclusive. If no odd
    integers exist in the specified range, the function returns 0.
  """
    total = 0
    for i in range(29, 80):
        if num_list[i] % 2 != 0:
            total += num_list[i]
    return total