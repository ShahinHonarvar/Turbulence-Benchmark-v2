def all_substring_of_size_n(str):
    """
    Write a function called 'all_substring_of_size_n' that takes one argument which is a string. The function should return the list of all distinct substrings of the length equal to 14 with no duplicate characters. If no such substrings exist in the given string, the function should return an empty list. The order of the substrings in the returned list does not matter.
    """
    substring = []
    for i in range(len(str) - 13):
        temp_substring = str[i:i + 14]
        if len(set(temp_substring)) == 14:
            substring.append(temp_substring)
    return substring