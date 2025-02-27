def all_substring_of_size_n(s):
    """
    Return a list of all distinct substrings of the length equal to 78 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    The order of the substrings in the returned list does not matter.
    """
    substring_size = 78
    result = set()
    for i in range(len(s) - substring_size + 1):
        substring = s[i:i + substring_size]
        if len(set(substring)) == substring_size:
            result.add(substring)
    return list(result)