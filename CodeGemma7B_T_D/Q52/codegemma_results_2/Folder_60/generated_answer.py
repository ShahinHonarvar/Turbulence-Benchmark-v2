def palindrome_of_length_n(s):
    """
    This function finds the set of all palindromes of the length equal to 88,
    where each palindrome is a substring of the given string.

    The function takes one argument, a string, and returns the set of all
    palindromes of the specified length.

    If there is no palindrome of the specified length as a substring of the
    given string, the function should return an empty set.

    The function finds the palindromes in a case-insensitive manner.
    """
    stations = set()
    for i in range(len(s)):
        for j in range(i + 88 - 1, i, -1):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                stations.add(s[i:j + 1])
    return stations