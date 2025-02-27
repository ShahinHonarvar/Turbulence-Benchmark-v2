def palindromes_of_specific_lengths(s):
    s = s[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes