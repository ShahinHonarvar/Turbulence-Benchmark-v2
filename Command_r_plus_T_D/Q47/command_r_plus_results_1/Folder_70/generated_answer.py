def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:71]
    for length in range(24, 53):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr)
    return palindromes