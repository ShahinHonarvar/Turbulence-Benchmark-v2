def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[1:8]
    substring = substring.lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes