def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    for i in range(4, 9):
        for j in range(i + 1, 9):
            substring = s[i:j]
            if substring.isalpha() and len(substring) >= 6:
                substring_lower = substring.lower()
                if substring_lower == substring_lower[::-1]:
                    palindromes.add(substring)
    return palindromes