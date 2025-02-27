def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[18:89].lower()
    for i in range(len(substring)):
        for j in range(i + 12, i + 15):
            if j > len(substring) or not substring[i:j].isalpha():
                continue
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes