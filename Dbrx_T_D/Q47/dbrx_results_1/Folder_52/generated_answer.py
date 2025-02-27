def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(13, 43):
        for i in range(44, 100 - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes