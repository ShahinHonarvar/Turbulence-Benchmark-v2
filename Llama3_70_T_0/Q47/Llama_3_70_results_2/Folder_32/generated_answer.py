def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for length in range(43, 48):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes