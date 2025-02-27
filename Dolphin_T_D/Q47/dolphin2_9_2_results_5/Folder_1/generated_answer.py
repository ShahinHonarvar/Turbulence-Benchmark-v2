def palindromes_of_specific_lengths(s):
    s = s[15:90]
    palindromes = set()
    for length in range(40, 73):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes