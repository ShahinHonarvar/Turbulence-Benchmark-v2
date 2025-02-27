def palindromes_between_indices(s: str) -> set[str]:
    palindromes = set()
    for i in range(5, min(len(s), 10)):
        substring = s[5:i]
        substring = ''.join(filter(str.isalpha, substring)).lower()
        if len(substring) >= 5 and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes