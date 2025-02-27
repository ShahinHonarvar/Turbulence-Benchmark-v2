def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[17:88]
    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr)
    return palindromes