def palindromes_of_specific_lengths(s):
    s = s.lower()[:51]
    palindromes = set()
    for length in range(50, 101):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes