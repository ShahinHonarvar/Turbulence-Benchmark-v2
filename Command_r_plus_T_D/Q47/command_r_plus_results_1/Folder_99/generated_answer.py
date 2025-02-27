def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[126:289].lower()
    palindromes = set()
    for length in range(119, 142):
        for start in range(len(substring) - length):
            end = start + length
            if substring[start:end] == substring[start:end][::-1] and substring[start:end].isalpha():
                palindromes.add(substring[start:end])
    return palindromes