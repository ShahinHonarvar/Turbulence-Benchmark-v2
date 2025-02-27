def all_substring_of_size_n(s):
    """This function takes one argument which is a string.
            The function should return the list of all distinct substrings of the length equal to 50 with no duplicate characters.
            If no such substrings exist in the given string, the function should return an empty list.
            The order of the substrings in the returned list does not matter."""
    result = []
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result