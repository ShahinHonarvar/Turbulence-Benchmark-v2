def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(12, 93):
        for length in range(42, 78):
            if i + length - 1 < len(s):
                substring = s[i:i + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes