def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[1:8].lower()
    for i in range(2, 8):
        for j in range(i + 1, 8 + 1):
            substring = s_lower[i:j]
            if substring == substring[::-1] and substring not in english_letters:
                palindromes.add(substring)
    return palindromes