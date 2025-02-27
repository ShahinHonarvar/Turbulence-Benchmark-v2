def palindromes_of_specific_lengths(s):
    s = s[34:91].lower()
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes