def all_substring_of_size_n(s):
    """
            This function returns the list of all distinct substrings of the length equal to 94 with no duplicate characters.
            """
    if len(s) < 94:
        return []
    result = set()
    for i in range(len(s) - 93):
        substring = s[i:i + 94]
        if len(set(substring)) == 94:
            result.add(substring)
    return list(result)