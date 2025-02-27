def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[14:95]
    palindromes = set()
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].isalpha() and substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes