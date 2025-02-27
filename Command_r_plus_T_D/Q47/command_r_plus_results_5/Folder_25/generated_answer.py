def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[25:85]
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes