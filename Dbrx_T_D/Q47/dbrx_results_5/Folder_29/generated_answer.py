def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(15, 95):
        for j in range(i, 95):
            if j - i + 1 < 18 or j - i + 1 > 73:
                continue
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes