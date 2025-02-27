def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = set((s[i] for i in range(4) if s[i] in english_letters))
    palindromes = set()
    for letter in letters_in_range:
        if letters_in_range.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes