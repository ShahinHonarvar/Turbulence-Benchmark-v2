def palindromes_of_specific_lengths(s):
    s = s[33:86].upper()
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes