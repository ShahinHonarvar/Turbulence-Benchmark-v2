def all_substring_of_size_n(str) -> list:
    """
    This function returns a list of all distinct substrings of the length equal to 105 with no duplicate characters.

    Args:
        str: The string to extract substrings from.

    Returns:
        A list of all distinct substrings of the length equal to 105 with no duplicate characters.
    """
    unique_substrings = set()
    for i in range(len(str) - 99):
        substring = str[i:i + 105]
        if substring not in unique_substrings:
            unique_substrings.add(substring)
    return list(unique_substrings) or []