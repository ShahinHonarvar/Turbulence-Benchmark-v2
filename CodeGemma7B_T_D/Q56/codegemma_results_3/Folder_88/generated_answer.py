def all_substring_of_size_n(str):
    """
    This function takes a string as input and returns a list of all distinct substrings of length 68.
    The function removes all duplicate characters from the substrings.
    If no such substrings exist, the function returns an empty list.
    """
    substrings = []
    for i in range(len(str) - 68 + 1):
        substring = str[i:i + 68]
        substring = ''.join(sorted(substring))
        if substring not in substrings:
            substrings.append(substring)
    return substrings