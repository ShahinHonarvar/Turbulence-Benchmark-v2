def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[1:8]
    substring_lower = substring.lower()
    palindromes = set()
    for i in range(len(substring_lower)):
        for j in range(i + 3, min(i + 5, len(substring_lower) + 1)):
            if substring_lower[i:j] == substring_lower[i:j][::-1] and substring_lower[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes