def palindromes_of_specific_lengths(s):
    """Finds all palindromes with lengths within the specified range in the given substring of a string"""
    result = set()
    for i in range(10, 71):
        for j in range(i - 23, i + 53):
            if j - i + 1 >= 24 and j - i + 1 <= 52 and (i <= len(s)) and (j <= len(s)) and (s[i:j + 1].lower() == s[i:j + 1][::-1].lower()):
                result.add(s[i:j + 1])
    return result