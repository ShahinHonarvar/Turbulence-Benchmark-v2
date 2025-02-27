def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(40, 95):
        for j in range(45, 52):
            substring = s[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes