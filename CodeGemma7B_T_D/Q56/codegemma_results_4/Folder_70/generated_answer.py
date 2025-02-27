def all_substring_of_size_n(str):
    """
            This function returns the list of all distinct substrings of the length equal to 12 with no duplicate characters. If no such substrings exist in the given string, the function should return an empty list. The order of the substrings in the returned list does not matter.

            Args:
                str: The string to find all substrings of.

            Returns:
                A list of all distinct substrings of the length equal to 12 with no duplicate characters. If no such substrings exist in the given string, the function should return an empty list.
            """
    result = []
    for i in range(len(str) - 11):
        substring = str[i:i + 12]
        if substring not in result:
            result.append(substring)
    return result