def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[3:8].lower()
    palindromes = set()
    for i in range(len(s_lower)):
        for j in range(i + 6, len(s_lower) + 1):
            substring = s_lower[i:j]
            if set(substring).issubset(english_letters) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes