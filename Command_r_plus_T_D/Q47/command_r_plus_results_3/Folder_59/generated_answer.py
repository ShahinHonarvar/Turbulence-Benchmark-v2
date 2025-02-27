def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    s = s[:101].lower()
    for length in range(3, 16):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes