def sum_even_ints_inclusive(int_list):
    """
  Takes one argument, a list of integers.
  Returns the sum of all even integers from index 42 to index 68, inclusive.
  If no even integers exist in the specified range, the function should return 0.
  """
    even_sum = 0
    for i in range(42, 69):
        if int_list[i] % 2 == 0:
            even_sum += int_list[i]
    return even_sum