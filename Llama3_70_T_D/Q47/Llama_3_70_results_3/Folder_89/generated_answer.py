def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[18:89]
    palindromes = set()
    for i in range(len(s) - 11):
        for length in range(12, 15):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes