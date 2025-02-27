def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[2:6].lower()
    letters_in_range = set(substring) & english_letters
    for letter in letters_in_range:
        if substring.count(letter) >= 2:
            palindromes.add(letter * 2)
        if substring.count(letter) >= 3:
            palindromes.add(letter * 3)
    return palindromes