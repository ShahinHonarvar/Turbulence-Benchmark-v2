def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:56].lower()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes