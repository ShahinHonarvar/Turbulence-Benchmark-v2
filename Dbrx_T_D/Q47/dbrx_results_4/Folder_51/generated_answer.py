def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(2, 9):
        for j in range(0, len(s) - i + 1):
            substring = s[j:j + i].lower()
            if substring.isalpha() and substring == substring[::-1] and (len(substring) in [3, 4]):
                palindromes.add(substring)
    return palindromes