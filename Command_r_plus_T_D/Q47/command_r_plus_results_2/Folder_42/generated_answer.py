def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[42:96].lower()
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes