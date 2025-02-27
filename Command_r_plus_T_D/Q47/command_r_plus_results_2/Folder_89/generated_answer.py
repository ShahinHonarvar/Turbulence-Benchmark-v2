def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[17:89].lower()
    for i in range(len(substring)):
        for j in range(i + 11, i + 15):
            if j < len(substring) and substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes