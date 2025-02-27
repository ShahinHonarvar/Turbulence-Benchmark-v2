def palindromes_of_specific_lengths(s):
    s = s[10:60]
    palindromes = set()
    for length in range(18, 37):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes