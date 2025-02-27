def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[30:75].lower()
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes