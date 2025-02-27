def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[15:87].lower()
    for i in range(51, 61):
        for j in range(len(substring) - i + 1):
            substr = substring[j:j + i]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes