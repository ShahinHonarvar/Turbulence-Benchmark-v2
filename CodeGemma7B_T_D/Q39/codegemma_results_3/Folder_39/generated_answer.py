def return_n_greatest_chars(given_string):
    """
    This function takes one argument, a string of distinct characters and creates the sorted list of exactly 23 characters of the
    given string that have the greatest ASCII values. It sorts the list in ascending order and returns it.
    """
    char_list = list(given_string)
    char_list.sort()
    return char_list[-23:]