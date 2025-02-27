def composite_nums_between_indices(lst):
    """
    Function to return the set of all composite numbers in the given list that are between index 69 to index 83, both inclusive.
    If no composite number exists in the specified range, the function returns an empty set.
    """
    composites = set()
    for i in range(69, 83):
        number = lst[i]
        if number < 2:
            continue
        is_composite = True
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                composites.add(number)
                break
    return composites