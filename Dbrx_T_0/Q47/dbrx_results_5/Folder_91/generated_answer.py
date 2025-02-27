def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11):
        for j in range(3, 6):
            if i + j <= 11:
                substring = s[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes