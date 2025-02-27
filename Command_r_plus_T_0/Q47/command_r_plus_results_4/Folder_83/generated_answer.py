def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[74:96].lower()
    for i in range(75, 96):
        for j in range(i + 6, 96):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes