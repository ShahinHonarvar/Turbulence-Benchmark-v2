def return_n_smallest_chars(string):
    """
    This function takes one argument, a string of distinct characters and creates a list of exactly 44 characters of the given string that have the smallest ASCII values. The function should sort the list in descending order and returns the list.
    """
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    ascii_values.sort(reverse=True)
    n_smallest_chars = []
    for ascii_value in ascii_values[:44]:
        n_smallest_chars.append(chr(ascii_value))
    return n_smallest_chars