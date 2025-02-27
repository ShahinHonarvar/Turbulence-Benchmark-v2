def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[10:88].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 4, i + 6):
            if j < len(substring) and substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes