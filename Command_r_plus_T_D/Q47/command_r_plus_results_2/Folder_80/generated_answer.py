def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[34:89].lower()
    for length in range(24, 34):
        for i in range(len(substring) - length):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes