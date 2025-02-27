from functools import cmp_to_key

def return_n_smallest_chars(string):
    """This function returns a list of 43 characters from the given string with the smallest ASCII values. The list is sorted in ascending order."""
    return sorted(string, key=cmp_to_key(lambda char1, char2: ord(char1) - ord(char2)))[:43]