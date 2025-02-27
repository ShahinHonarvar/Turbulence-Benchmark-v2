def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(28, 95):
        for j in range(38, 50):
            if i + j - 1 <= 94:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes