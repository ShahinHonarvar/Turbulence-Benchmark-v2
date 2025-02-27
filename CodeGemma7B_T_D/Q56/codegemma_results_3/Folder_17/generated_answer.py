def all_substring_of_size_n(string, n):
    """Returns the list of all distinct substrings of the length equal to n with no duplicate characters."""
    if len(string) < n:
        return []
    unique_substrings = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if all((char not in substring for char in substring)):
            unique_substrings.add(substring)
    return list(unique_substrings)