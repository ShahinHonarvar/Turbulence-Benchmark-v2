def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[30:85]
    palindromes = set()
    for length in range(12, 21):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr)
    return palindromes