def all_substring_of_size_n(s):
    """
    Write a function called 'all_substring_of_size_n' that takes one argument which is a string.
    The function should return the list of all distinct substrings of the length equal to 16 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    The order of the substrings in the returned list does not matter.
    """
    return [s[i:i + 16] for i in range(len(s) - 15) if len(set(s[i:i + 16])) == 16]