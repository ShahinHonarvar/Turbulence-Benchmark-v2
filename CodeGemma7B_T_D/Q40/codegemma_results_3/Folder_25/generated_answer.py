from functools import cmp_to_key

def return_n_smallest_chars(char_string):
    """
    Returns a list of the n smallest characters in a string.
    """
    char_list = list(char_string)
    char_list.sort(key=cmp_to_key(lambda x, y: ord(x) - ord(y)))
    return char_list[:29]