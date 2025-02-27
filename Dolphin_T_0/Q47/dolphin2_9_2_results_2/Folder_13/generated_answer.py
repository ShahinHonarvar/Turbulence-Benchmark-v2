def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    result = set()
    for length in range(57, 61):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                if substring == substring[::-1]:
                    result.add(substring)
    return result