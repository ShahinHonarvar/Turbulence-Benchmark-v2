def all_substring_of_size_n(str):
    """
    This function takes one argument which is a string.
    The function should return the list of all distinct substrings of the length equal to 9 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    The order of the substrings in the returned list does not matter.
    """
    str = str.lower()
    list = []
    for i in range(0, len(str)):
        for j in range(i + 1, len(str)):
            for k in range(j + 1, len(str)):
                for l in range(k + 1, len(str)):
                    for m in range(l + 1, len(str)):
                        for n in range(m + 1, len(str)):
                            for o in range(n + 1, len(str)):
                                for p in range(o + 1, len(str)):
                                    if len(set(str[i:p + 1])) == 9:
                                        list.append(str[i:p + 1])
    return list