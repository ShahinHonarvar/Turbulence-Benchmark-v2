def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[63:71].lower()
    palindromes = set()
    for i in range(6, 7):
        for j in range(i + 4, i + 6):
            if j <= len(substring):
                sub = substring[i:j]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    return palindromes