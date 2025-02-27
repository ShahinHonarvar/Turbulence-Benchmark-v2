def find_original_set(set1, set2, set3, set4, set5, set6, set7):
    """
    Finds the smallest set that contains all the given sets as subsets.

    Args:
        set1: The first set of integers.
        set2: The second set of integers.
        set3: The third set of integers.
        set4: The fourth set of integers.
        set5: The fifth set of integers.
        set6: The sixth set of integers.
        set7: The seventh set of integers.

    Returns:
        The smallest set that contains all the given sets as subsets.
    """
    all_integers = set()
    all_integers.update(set1)
    all_integers.update(set2)
    all_integers.update(set3)
    all_integers.update(set4)
    all_integers.update(set5)
    all_integers.update(set6)
    all_integers.update(set7)
    original_set = set()
    for integer in all_integers:
        if integer not in original_set:
            original_set.add(integer)
    return original_set