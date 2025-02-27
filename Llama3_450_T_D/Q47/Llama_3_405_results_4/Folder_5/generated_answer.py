def palindromes_of_specific_lengths(s):
    s = s[63:71]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.casefold() == substring.casefold()[::-1]:
                palindromes.add(substring)
    return palindromes