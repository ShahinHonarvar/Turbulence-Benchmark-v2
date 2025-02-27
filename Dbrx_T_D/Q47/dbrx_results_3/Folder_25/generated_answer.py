def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    for i in range(26, 85):
        for j in range(30, 47):
            if i + j - 1 <= 84:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes