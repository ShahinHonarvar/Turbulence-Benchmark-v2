def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[5:10].lower()
    s_lower_set = set(s_lower)
    if s_lower_set.issubset(english_letters):
        for i in range(len(s_lower) - 3):
            if s_lower[i] == s_lower[i + 3] or (i + 1 < len(s_lower) and s_lower[i] == s_lower[i + 2]):
                palindromes.add(s_lower[i:i + 3])
    return palindromes