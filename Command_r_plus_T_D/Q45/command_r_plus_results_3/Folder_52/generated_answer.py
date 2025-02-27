def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    chars_between_indices = set((s[i] for i in range(8) if s[i] in english_letters))
    palindromes = set()
    for p_length in range(6, 9):
        for p in chars_between_indices ** p_length:
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes