def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    palindromes = set()
    for start in range(7):
        for length in range(3, 7):
            end = start + length
            if end > 7:
                break
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes