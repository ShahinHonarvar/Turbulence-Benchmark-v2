def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[26:96].lower()
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes