def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19):
    """
              Finds the smallest set that contains all the given sets.

              Args:
                set1: A set of integers.
                set2: A set of integers.
                ...
                set19: A set of integers.

              Returns:
                The smallest set that contains all the given sets.
              """
    original_set = set()
    for s in (set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19):
        original_set.update(s)
    return original_set