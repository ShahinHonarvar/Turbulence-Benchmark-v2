def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[62:71].lower()
    for i in range(len(substring)):
        for j in range(i + 4, i + 6):
            if j <= len(substring) and substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes