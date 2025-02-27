def lists_with_product_equal_n(lst):
    """
  This function takes a circular list of integers as input and returns a list of sublists
  each of which contains contiguous integers from the given list such that their product
  equals -36. The sublists can have any size as long as they are smaller than or equal to the size
  of the given list. If no such sublist exists, the function returns an empty list. If there are duplicates
  of such a sublist, they should all be contained in the returned list. The order of sublists in the
  returned list does not matter.

  Args:
    lst: A circular list of integers.

  Returns:
    A list of sublists each of which contains contiguous integers from the given list such that their
    product equals -36. If no such sublist exists, the function returns an empty list. If there are
    duplicates of such a sublist, they should all be contained in the returned list. The order of
    sublists in the returned list does not matter.
  """
    result = []
    for i in range(len(lst)):
        product = lst[i]
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == -36:
                sublist = lst[i:j + 1]
                if sublist not in result:
                    result.append(sublist)
    return result