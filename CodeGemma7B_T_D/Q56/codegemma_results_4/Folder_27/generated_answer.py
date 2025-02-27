def all_substring_of_size_n(str):
    """
    This function returns all distinct substrings of the length
    of 57 with no duplicate characters. If no such substrings
    exist in the given string, the function returns an empty list.
    """
    substrings = []
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            substring = str[i:j + 1]
            if len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings