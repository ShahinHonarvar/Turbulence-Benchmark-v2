def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    palindromes = set()
    for i in range(3, 5):
        for j in range(5 - i + 1):
            substring = s[j:j + i]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes