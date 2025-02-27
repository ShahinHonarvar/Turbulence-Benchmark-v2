def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, min(i + 6, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes