def all_substring_of_size_n(s: str) -> list[str]:
    """
    It takes a string as input and returns the list of all the substrings of the string with a length of 6.
    """
    res = []
    if len(s) > 5:
        for i in range(len(s) - 5):
            substring = s[i:i + 6]
            if substring not in res:
                res.append(substring)
    return res