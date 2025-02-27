def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:56].lower()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes