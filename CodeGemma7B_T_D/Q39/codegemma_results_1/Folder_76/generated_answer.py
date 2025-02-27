def return_n_greatest_chars(input_str):
    """
    Returns a sorted list of the 3 characters that have the greatest ASCII values.
    """
    char_list = list(input_str)
    char_list.sort(key=ord, reverse=True)
    return char_list[:3]