def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[36:93]
    palindromes = set()
    for i in range(10, 36):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes