def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[29:99]
    for length in range(6, 10):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes