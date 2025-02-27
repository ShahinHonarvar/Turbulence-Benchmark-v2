def palindromes_of_specific_lengths(s):
    s = s[10:60]
    result = set()
    for length in range(18, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    result.add(substring.lower())
    return result