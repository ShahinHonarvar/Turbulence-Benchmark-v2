def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:101]
    for length in range(10, 51):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                substring = substring.lower()
                if substring == substring[::-1]:
                    result.add(substring)
    return result