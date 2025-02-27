def all_substring_of_size_n(str):
    """
            Write a function called 'all_substring_of_size_n' that takes one argument which is a string.
            The function should return the list of all distinct substrings of the length equal to 89 with no duplicate characters.
            If no such substrings exist in the given string, the function should return an empty list.
            The order of the substrings in the returned list does not matter.
            """
    res = []
    if len(str) < 89:
        return res
    for i in range(len(str) - 88):
        res.append(str[i:i + 89])
    return list(set(res))