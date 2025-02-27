def palindromes_of_specific_lengths(s):
    s = s[17:89].lower()
    palindromes = set()
    for i in range(12, 15):
        for j in range(0, len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes