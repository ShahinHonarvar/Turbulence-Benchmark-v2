def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[70:141]
    cleaned = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(cleaned)):
        for j in range(i + 3, min(i + 61, len(cleaned) + 1)):
            substr = cleaned[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result