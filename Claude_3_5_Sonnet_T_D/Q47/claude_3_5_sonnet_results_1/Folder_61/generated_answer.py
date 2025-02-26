def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    for i in range(31):
        for j in range(i + 20, min(i + 31, 32)):
            substr = s[i:j]
            if substr == substr[::-1] and 20 <= len(substr) <= 30:
                result.add(substr)
    return result