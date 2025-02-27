def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_between_indices = set((s[i].lower() for i in range(2, 10) if s[i].isalpha()))
    palindromes = set()
    for letter in letters_between_indices:
        if letters_between_indices.issubset(english_letters) and len(letters_between_indices) >= 4:
            palindromes.add(letter * 2)
    return palindromes