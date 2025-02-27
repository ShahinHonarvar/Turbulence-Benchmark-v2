def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(44, 99 + 1):
        for j in range(i, i + 13, 1):
            for k in range(j, i - 13, -1):
                substring = s[i:k + 1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes