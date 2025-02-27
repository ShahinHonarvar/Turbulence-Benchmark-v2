def all_odd_ints_exclusive(list_of_integers):
    """
  Returns a list of all odd integers from index 20 to index 200, both exclusive.
  If no odd integers exist in the specified range, the function
  should return an empty list.
  """
    odd_numbers = []
    for number in list_of_integers[20:200]:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers