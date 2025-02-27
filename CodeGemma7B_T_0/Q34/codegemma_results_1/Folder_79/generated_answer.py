def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17):
    """
            This function takes 17 sets of integers as input and returns the smallest set that contains all of the input sets as subsets.
            """
    original_set = set()
    for s in (set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17):
        original_set.update(s)
    return original_set