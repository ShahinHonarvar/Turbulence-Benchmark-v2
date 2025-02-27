def all_substring_of_size_n(text):
    """
    Return a list of all distinct substrings of size 42 with no duplicate characters.
    """
    if len(text) < 42:
        return []
    substrings = set()
    for i in range(len(text) - 41):
        substring = text[i:i + 42]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)