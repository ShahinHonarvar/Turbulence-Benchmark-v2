def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(27, 78):
        for j in range(i, i + 20):
            if j <= 77:
                substring = s[i:j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes