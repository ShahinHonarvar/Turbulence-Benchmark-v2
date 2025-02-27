def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[21:96].lower()
    for i in range(len(substring)):
        for j in range(i + 51, min(i + 55, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes