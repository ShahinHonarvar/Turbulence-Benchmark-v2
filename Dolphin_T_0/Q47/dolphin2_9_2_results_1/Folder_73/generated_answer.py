def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[21:63]
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr.lower() == substr.lower()[::-1] and all((c.isalpha() for c in substr)):
                palindromes.add(substr)
    return palindromes