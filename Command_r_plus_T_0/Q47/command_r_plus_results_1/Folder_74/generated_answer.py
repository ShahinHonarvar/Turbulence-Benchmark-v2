def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[30:85].lower()
    for length in range(12, 21):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes