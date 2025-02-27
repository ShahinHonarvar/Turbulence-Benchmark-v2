def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[200:301].lower()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes