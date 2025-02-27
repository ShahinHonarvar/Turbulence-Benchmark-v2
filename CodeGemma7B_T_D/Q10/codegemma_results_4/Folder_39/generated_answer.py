from index [start_idx] (inclusive) to index [end_idx] (exclusive).

def all_odd_ints_exclusive(lst, start_idx=43, end_idx=99):
    """
  This function takes a list of integers and returns the list of all odd integers
  If no odd integers exist in the specified range, the function returns an empty list.
  """
    result = []
    for i in range(start_idx, end_idx):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result