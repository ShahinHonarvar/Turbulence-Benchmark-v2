def palindromes_of_specific_lengths(s):
    s = s[12:100].lower()
    lengths = range(26, 30)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes