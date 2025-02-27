def palindromes_of_specific_lengths(s):
    s = s[11:123]
    palindromes = set()
    for length in range(12, 221):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring.lower() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes