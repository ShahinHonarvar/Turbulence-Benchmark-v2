def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[2:10].lower()
    palindromes = set()
    for i in range(3, len(s_lower) // 2 + 1):
        for j in range(len(s_lower) - i + 1):
            substring = s_lower[j:j + i]
            if set(substring).issubset(english_letters) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes