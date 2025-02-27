def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[17:88].lower()
    for i in range(50, 26, -1):
        for j in range(len(substring) - i + 1):
            substr = substring[j:j + i]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes