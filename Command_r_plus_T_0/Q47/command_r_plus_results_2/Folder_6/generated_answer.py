def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[44:99].lower()
    palindromes = set()
    for length in range(40, 48):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes