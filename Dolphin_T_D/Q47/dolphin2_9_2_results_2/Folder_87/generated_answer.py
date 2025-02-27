def palindromes_of_specific_lengths(s):
    s = s[11:94]
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                palindromes.add(substr.lower())
    return palindromes