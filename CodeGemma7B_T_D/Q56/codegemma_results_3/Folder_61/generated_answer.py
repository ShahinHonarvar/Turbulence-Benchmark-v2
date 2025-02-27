def all_substring_of_size_n(str):
    """
    This function returns a list of all distinct substrings of the length equal to 39 with no duplicate characters.
    """
    result = []
    for i in range(len(str) - 38):
        substring = str[i:i + 39]
        if len(set(substring)) == 39:
            result.append(substring)
    return result