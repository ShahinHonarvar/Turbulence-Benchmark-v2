def all_substring_of_size_n(string):
    """
            This function takes one argument which is a string.
            The function returns the list of all distinct substrings
            of the length equal to 17 with no duplicate characters.
            If no such substrings exist in the given string,
            """
    substring_list = []
    for i in range(len(string)):
        for j in range(i + 17, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 17 and substring not in substring_list:
                substring_list.append(substring)
    return substring_list