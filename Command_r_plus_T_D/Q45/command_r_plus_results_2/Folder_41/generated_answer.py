def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_between_indices = {char for char in s[2:4] if char in english_letters}
    for letter in letters_between_indices:
        if s[2:4].count(letter) >= 2:
            palindromes.add(letter * 2)
        if s[2:4].count(letter) >= 3:
            palindromes.add(letter * 3)
    return palindromes