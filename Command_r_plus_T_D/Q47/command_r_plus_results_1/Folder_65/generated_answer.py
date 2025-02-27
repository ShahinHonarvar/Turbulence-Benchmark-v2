def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[14:96]
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes