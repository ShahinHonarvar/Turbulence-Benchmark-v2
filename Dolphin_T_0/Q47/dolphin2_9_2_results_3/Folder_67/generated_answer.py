def palindromes_of_specific_lengths(s):
    substring = s[65:100]
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                palindromes.add(substr)
    return palindromes