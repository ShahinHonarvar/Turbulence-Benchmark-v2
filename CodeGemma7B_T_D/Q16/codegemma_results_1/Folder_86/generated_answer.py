def sum_even_ints_inclusive(num_list):
    """Sum of even integers in a list between indices 31 and 34 (inclusive)

  Args:
    num_list (list): A list of integers.

  Returns:
    int: The sum of even integers in the specified range, or 0 if no even integers exist.
  """
    total = 0
    for i in num_list[31:35]:
        if i % 2 == 0:
            total += i
    return total