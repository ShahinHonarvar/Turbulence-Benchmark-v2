def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:88].lower()
    for i in range(len(substring)):
        for j in range(i + 4, min(i + 6, len(substring) + 1)):
            if substring[i:j] == substring[i + 1:j - 1] == substring[i + 2:j - 2] == substring[i + 3:j - 3]:
                if substring[i:j].isalpha():
                    palindromes.add(substring[i:j])
    return palindromes