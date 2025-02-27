def find_original_set(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
    """
            Finds the smallest set that contains all of the given sets.

            Args:
                *a1, *a2, ..., *a16: Sets of integers.

            Returns:
                The smallest set containing all of the given sets.
            """
    intersection = a1
    for set in [a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16]:
        intersection = intersection.intersection(set)
    return intersection