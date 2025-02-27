def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(7):
        for j in range(i + 4, min(i + 6, len(s))):
            substring = s[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes