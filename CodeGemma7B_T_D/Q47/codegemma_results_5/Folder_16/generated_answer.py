def palindromes_of_specific_lengths(s):
    """
    Given a string, returns the set of all palindromes with specific lengths and indices.
    """
    result = set()
    s = s.lower()
    for i in range(15, 87):
        for j in range(i, 87):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 51 and (len(substring) <= 60):
                result.add(substring)
    return result