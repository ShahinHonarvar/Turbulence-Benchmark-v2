def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(26, 30):
        for start in range(13, 100 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes