def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[16:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes