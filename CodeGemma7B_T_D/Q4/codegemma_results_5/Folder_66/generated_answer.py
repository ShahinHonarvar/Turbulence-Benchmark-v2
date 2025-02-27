def all_pos_ints_exclusive(user_input):
    """
    This function returns a list of all positive integers from index 13 to index 76,
    both exclusive. If no positive integers exist in the specified range, the function
    will return an empty list.
    """
    if not any((num > 0 for num in user_input)):
        return []
    return user_input[12:76]