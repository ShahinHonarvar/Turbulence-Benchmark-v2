def find_n_th_smallest_num(arr):
    """
  Finds the nth smallest number from index m to n, inclusive.

  Args:
    arr: A list of distinct numbers.
    n: The index of the smallest number to return.
    m: The starting index of the search range.
    n: The ending index of the search range.

  Returns:
    The nth smallest number from index m to n, inclusive.
  """
    arr.sort()
    index = m + n - 2
    return arr[index]