def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_between_indices = set((s[i].lower() for i in range(3, 9) if s[i].isalpha()))
    palindromes = set()
    for letter in letters_between_indices:
        if letters_between_indices.issubset(english_letters):
            if len(letters_between_indices) >= 5:
                palindromes.add(''.join(letters_between_indices))
    return palindromes