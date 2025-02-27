def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[1:7].lower()
    letters_in_range = set(s_lower) & english_letters
    palindromes = set()
    for letter in letters_in_range:
        if s_lower.count(letter) > 1:
            palindromes.add(letter * 2)
    return palindromes