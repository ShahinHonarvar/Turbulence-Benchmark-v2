def return_n_smallest_chars(str):
    """
    funtion to create a list of the 60 characters with the smallest ascii values from a string
    """
    str_list = list(str)
    str_list.sort()
    return str_list[:60]