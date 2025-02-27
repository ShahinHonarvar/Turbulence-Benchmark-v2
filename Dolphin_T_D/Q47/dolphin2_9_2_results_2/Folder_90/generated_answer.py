def palindromes_of_specific_lengths(s):
    substring = s[105:280]
    palindromes = set()
    for length in range(136, 152):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if all((c.isalpha() for c in substr)) and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes