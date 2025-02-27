def all_substring_of_size_n(string):
    """
    Returns the list of all distinct substrings of the length equal to 142 with no duplicate characters. If no such substrings exist in the given string, the function should return an empty list. The order of the substrings in the returned list does not matter.
    """
    return [substring for substring in [string[i:i + 142] for i in range(len(string) - 142 + 1)] if len(set(substring)) == 142]