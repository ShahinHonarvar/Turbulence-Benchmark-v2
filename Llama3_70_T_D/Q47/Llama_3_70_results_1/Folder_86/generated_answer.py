def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[30:96]
    palindromes = set()
    for length in range(34, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes