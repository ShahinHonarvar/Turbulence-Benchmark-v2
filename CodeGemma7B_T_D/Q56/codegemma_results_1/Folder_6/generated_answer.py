def all_substring_of_size_n(s):
    """
            Returns a list of all distinct substrings of the length equal to 23 with no duplicate characters.
            """
    result = []
    for i in range(len(s) - 23 + 1):
        substring = s[i:i + 23]
        if len(set(substring)) == 23:
            result.append(substring)
    return result