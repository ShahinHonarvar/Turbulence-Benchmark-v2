def all_substring_of_size_n(input_str):
    """Returns a list of all the distinct substrings of length equal to 25 with no duplicate characters.

    Args:
        input_str: The string to generate substrings from.

    Returns:
        A list of substrings of length equal to 25 with no duplicate characters, or an empty list if no such substrings exist.
    """
    if len(input_str) < 25:
        return []
    unique_substrings = set()
    for i in range(len(input_str) - 24):
        substring = input_str[i:i + 25]
        if len(set(substring)) == 25:
            unique_substrings.add(substring)
    return list(unique_substrings)