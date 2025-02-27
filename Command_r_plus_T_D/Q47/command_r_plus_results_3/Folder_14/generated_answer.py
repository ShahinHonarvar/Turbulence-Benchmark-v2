def palindromes_of_specific_lengths(s: str) -> set:
    s = s[10:75].lower()
    palindromes = set()
    for length in range(6, 9):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes