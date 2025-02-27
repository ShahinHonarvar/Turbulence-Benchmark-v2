def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[42:96].lower()
    palindromes = set()
    for length in range(18, 48):
        for start in range(len(substring) - length + 1):
            end = start + length
            if substring[start:end] == substring[start:end][::-1] and substring[start:end].isalpha():
                palindromes.add(substring[start:end])
    return palindromes