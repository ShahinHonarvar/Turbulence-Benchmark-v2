def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_between_indices = set((s[i].lower() for i in range(7) if s[i].isalpha()))
    palindromes = set()
    for letter in letters_between_indices:
        if letters_between_indices.issubset(english_letters) and letters_between_indices.intersection(english_letters).count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes