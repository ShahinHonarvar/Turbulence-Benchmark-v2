def composite_nums_between_indices(lst):
    """
  This function takes a list of positive integers and returns the set of all composite numbers in the given list between index 0 to index 6, both inclusive.
  """
    composite_nums = set()
    for i in range(0, 7):
        if lst[i] > 1 and (not all((lst[i] % j for j in range(2, int(lst[i] ** 0.5) + 1)))):
            composite_nums.add(lst[i])
    return composite_nums