def palindromes_of_specific_lengths(s):
    s = s[15:61]
    result = set()
    for length in range(16, 40):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    result.add(substring)
    return result