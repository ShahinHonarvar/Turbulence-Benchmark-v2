def all_substring_of_size_n(str):
    """
    write a function called 'all_substring_of_size_n' that takes one argument which is a string.
    The function should return the list of all distinct substrings of the length equal to 99 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    """
    result = set()
    for i in range(len(str) - 2):
        for j in range(i + 1, len(str) - 2):
            if len(set(str[i:j + 1])) == 99:
                result.add(str[i:j + 1])
    return list(result)