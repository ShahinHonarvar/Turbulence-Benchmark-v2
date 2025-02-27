def palindromes_of_specific_lengths(s):
    s = s[23:83].lower()
    palindromes = set()
    for i in range(len(s) - 31):
        for j in range(32, 35):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes