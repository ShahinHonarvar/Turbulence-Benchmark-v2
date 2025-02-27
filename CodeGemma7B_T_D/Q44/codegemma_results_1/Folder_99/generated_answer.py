def composite_nums_between_indices(lst):
    """
  This function takes an list of positive integers and returns the set of all composite numbers in the given list
  that are between index 246 to index 750, both inclusive. If no composite number exists in the specified range,
  the function should return an empy set.
  """
    composite_nums = set()
    for i in range(246, 751):
        if lst[i] % 5 == 0:
            composite_nums.add(lst[i])
        elif lst[i] % 3 == 0:
            composite_nums.add(lst[i])
    return composite_nums