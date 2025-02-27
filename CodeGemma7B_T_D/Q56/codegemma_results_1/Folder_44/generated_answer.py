def all_substring_of_size_n(str):
    """
            This function takes one argument which is a string.
            The function should return the list of all distinct substrings of the length equal to 90 with no duplicate characters.
            If no such substrings exist in the given string, the function should return an empty list.
            The order of the substrings in the returned list does not matter.
            """
    unique_substrings = []
    for i in range(len(str) - 90 + 1):
        for j in range(i + 90):
            substring = str[i:j + 1]
            if substring not in unique_substrings:
                unique_substrings.append(substring)
    return unique_substrings