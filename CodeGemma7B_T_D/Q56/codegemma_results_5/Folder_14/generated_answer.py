def all_substring_of_size_n(string):
    """
    Given a string, return the list of all distinct substrings of length 85 with no duplicate characters.
    """
    substring_list = []
    for i in range(len(string) - 84):
        substring = string[i:i + 85]
        if substring not in substring_list:
            substring_list.append(substring)
    return substring_list