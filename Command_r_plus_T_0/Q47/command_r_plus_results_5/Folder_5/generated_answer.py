def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[63:71].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 4, min(i + 6, len(substring)) + 1):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes