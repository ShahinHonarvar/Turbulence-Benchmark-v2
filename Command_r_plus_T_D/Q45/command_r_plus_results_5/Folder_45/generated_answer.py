def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[5:10].lower()
    english_letters_in_s = set(s_lower) & english_letters
    palindromes = set()
    for letter in english_letters_in_s:
        if s_lower.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes