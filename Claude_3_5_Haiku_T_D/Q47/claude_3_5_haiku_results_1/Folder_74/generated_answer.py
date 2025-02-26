def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(12, 21):
        for start in range(30, 85 - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    result.add(substring)
    return result