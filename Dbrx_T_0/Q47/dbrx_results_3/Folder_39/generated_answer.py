def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(31, 92):
        for j in range(50, 54):
            if i + j - 1 <= 91:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes