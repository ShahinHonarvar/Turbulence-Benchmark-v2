def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_between_indices = {char for char in s[4:8] if char in english_letters}
    for letter in letters_between_indices:
        if letters_between_indices.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes