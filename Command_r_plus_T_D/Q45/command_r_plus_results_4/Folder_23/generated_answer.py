def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_between_indices = set((s[i] for i in range(7) if s[i] in english_letters))
    palindromes = set()
    for letter in letters_between_indices:
        for i in range(len(s) - 1):
            if s[i] == letter and s[i + 1] == letter:
                palindromes.add(s[i:i + 2].lower())
                break
    return palindromes