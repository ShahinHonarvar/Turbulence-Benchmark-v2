def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(14, 91 - 54):
        for length in range(55, 72):
            substring = s[start:start + length]
            if len(substring) == length and substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes