def all_pos_ints_inclusive(lst):
    """
            Returns a list of all positive integers from index 0 to index 7, both inclusive, from a given list.
            If no positive integers exist in the specified range, the function returns an empty list.
            """
    positive_found = False
    for num in lst:
        if num > 0:
            positive_found = True
            break
    if not positive_found:
        return []
    positive_nums = []
    for i in range(0, 8):
        if lst[i] > 0:
            positive_nums.append(lst[i])
    return positive_nums