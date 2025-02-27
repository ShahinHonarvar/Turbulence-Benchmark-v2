def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_letters_in_s = set((c.lower() for c in s[1:8] if c.lower() in english_letters))
    for p_length in range(6, len(english_letters_in_s) + 1):
        for p in english_letters_in_s:
            if english_letters_in_s.issubset(set((p.lower() for p in [s[1:8]]))):
                palindromes.add(p + p[::-1])
    return palindromes