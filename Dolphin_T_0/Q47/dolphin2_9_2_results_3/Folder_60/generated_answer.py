def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(23, 83):
        for j in range(i, 83):
            substring = s[i:j + 1].lower()
            if len(substring) in range(32, 35) and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes