def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_between_indices = set((s[i] for i in range(4, 7) if s[i] in english_letters))
    palindromes = set()
    for letter in letters_between_indices:
        if letters_between_indices.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes