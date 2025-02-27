def all_substring_of_size_n(text):
    """
            Returns a list of all distinct substrings of the length equal to n with no duplicate characters.
            """
    result = set()
    for i in range(len(text) - 2):
        substr = text[i:i + 3]
        if len(set(substr)) == len(substr):
            result.add(substr)
    if not result:
        return []
    return list(result)