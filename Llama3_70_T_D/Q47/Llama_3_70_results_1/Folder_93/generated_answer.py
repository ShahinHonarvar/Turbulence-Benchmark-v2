def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(13, 50):
        for i in range(17, 96 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes