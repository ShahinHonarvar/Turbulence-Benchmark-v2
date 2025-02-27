def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[15:95]
    palindromes = set()
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes