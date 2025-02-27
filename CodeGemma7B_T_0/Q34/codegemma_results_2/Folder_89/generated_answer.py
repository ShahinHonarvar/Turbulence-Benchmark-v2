def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29, set30, set31, set32, set33, set34, set35, set36, set37):
    """
  Finds the smallest set that contains all the given sets as subsets.

  Args:
    set1: The first set of integers.
    set2: The second set of integers.
    set3: The third set of integers.
    ...
    set37: The thirty-seventh set of integers.

  Returns:
    The smallest set that contains all the given sets as subsets.
  """
    original_sets = {set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29, set30, set31, set32, set33, set34, set35, set36, set37}
    all_elements = set()
    for s in original_sets:
        all_elements.update(s)
    sorted_elements = sorted(all_elements)
    smallest_set = set()
    for element in sorted_elements:
        if element not in smallest_set:
            smallest_set.add(element)
    if all((s <= smallest_set for s in original_sets)):
        return smallest_set
    else:
        return None