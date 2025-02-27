from collections import defaultdict

def all_substring_of_size_n(str):
    """
    Write a function called 'all_substring_of_size_n' that takes one argument which is a string.
    The function should return the list of all distinct substrings of the length equal to 16 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    The order of the substrings in the returned list does not matter.
    """
    result = []
    for start in range(len(str) - 15):
        substr = str[start:start + 16]
        if len(set(substr)) == 16:
            result.append(substr)
    return result