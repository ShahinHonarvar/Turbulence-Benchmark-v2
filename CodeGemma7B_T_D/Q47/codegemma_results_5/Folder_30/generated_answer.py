def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for i in range(14, 91):
        for j in range(i + 54, i + 72):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes