def palindrome_of_length_n(s):
    """
    Returns the set of all palindromes of length 113 composed of the given string.
    """
    lowercase_s = s.lower()
    result = set()
    for i in range(len(lowercase_s) - 112):
        for j in range(i + 113, len(lowercase_s) + 1):
            substring = lowercase_s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result