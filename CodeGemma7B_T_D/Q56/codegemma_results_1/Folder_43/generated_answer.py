def all_substring_of_size_n(str):
    """Returns all distinct substrings of the length equal to 6 with no duplicate characters.
            """
    result = set()
    for i in range(len(str) - 86 + 1):
        current_substring = str[i:i + 86]
        if len(set(current_substring)) == 86:
            result.add(current_substring)
    return list(result)