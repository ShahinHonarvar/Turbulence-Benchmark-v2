def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(1, 8):
        for length in range(3, 5):
            if start + length > len(s):
                break
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes