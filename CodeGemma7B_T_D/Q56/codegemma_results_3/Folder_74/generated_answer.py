def all_substring_of_size_n(text):
    """
    Write a function called 'all_substring_of_size_n' that takes one argument which is a string.
    The function should return the list of all distinct substrings of the length equal to 97 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    The order of the substrings in the returned list does not matter.
    """
    substrings = []
    for i in range(len(text) - 97 + 1):
        substring = text[i:i + 97]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings