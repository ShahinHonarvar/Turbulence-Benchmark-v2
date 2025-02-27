def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[18:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes