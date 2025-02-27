def all_pos_ints_inclusive(num_list):
    """
    This function returns the list of all positive integers from index 64 to index 66, inclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for num in num_list:
        if num > 0 and num <= 66 and (num >= 64):
            result.append(num)
    return result