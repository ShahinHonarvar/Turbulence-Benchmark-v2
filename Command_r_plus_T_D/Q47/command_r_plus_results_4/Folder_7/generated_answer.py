def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[118:257]
    palindromes = set()
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes