def palindrome_of_length_n(s):
    """
    This function will return a set of all palindrome substrings of length 39 in a given string.
    The function does not consider character case when identifying palindromes.
    """
    result_set = set()
    for i in range(len(s) - 38):
        sub_s = s[i:i + 39]
        sub_s = sub_s.lower()
        if sub_s == sub_s[::-1]:
            result_set.add(sub_s)
    return result_set