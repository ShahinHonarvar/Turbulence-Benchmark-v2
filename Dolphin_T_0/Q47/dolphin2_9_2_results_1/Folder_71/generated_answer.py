def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(23, 37):
        for i in range(17, 66):
            substring = s[i:i + length]
            if substring == substring.lower() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes