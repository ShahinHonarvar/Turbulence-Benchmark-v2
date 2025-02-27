def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    english_letters_in_range = set((s[i].lower() for i in range(4, 8) if s[i].lower() in english_letters))
    palindromes = set()
    for p in english_letters_in_range:
        if english_letters_in_range.count(p) >= 2:
            palindromes.add(p * 2)
    return palindromes