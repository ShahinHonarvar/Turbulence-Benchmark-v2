def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[3:9].lower()
    english_letters_in_range = set(s_lower) & english_letters
    palindromes = set()
    for letter in english_letters_in_range:
        if s_lower.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes