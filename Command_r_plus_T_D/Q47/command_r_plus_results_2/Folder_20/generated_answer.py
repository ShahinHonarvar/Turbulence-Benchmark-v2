def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[20:75].lower()
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes