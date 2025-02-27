def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(65, 100 - 25):
        for j in range(i + 26, min(i + 34, 100 + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes