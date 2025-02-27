def all_substring_of_size_n(string):
    """Returns list of all distinct substrings of the length equal to n with no duplicate characters.
  If no such substrings exist in the given string, the function should return an empty list.
  The order of the substrings in the returned list does not matter."""
    result = []
    for i in range(len(string) - 53 + 1):
        substring = string[i:i + 53]
        if substring not in result and len(set(substring)) == 53:
            result.append(substring)
    return result