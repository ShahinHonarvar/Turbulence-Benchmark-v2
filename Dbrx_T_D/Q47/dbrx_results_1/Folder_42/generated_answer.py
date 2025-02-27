def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(43, 96):
        for j in range(18, 48):
            substring = s[i:i + j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes