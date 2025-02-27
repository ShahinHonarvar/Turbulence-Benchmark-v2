def all_substring_of_size_n(s):
    """
    This function takes a string and returns a list of all distinct substrings of the length equal to 58 with no duplicate characters.
    If no such substrings exist in the given string, the function returns an empty list.
    The order of the substrings in the returned list does not matter.
    """
    size = len(s)
    if size < 58:
        return []
    result = []
    for i in range(size - 58 + 1):
        substring = s[i:i + 58]
        if len(set(substring)) == 58:
            result.append(substring)
    return result