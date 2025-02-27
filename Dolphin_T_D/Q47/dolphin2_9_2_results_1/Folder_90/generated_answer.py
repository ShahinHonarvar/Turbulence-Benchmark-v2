def palindromes_of_specific_lengths(s):
    s = s[105:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if all((c.isalpha() for c in substr)) and substr.lower() == substr.lower()[::-1]:
                palindromes.add(substr)
    return palindromes