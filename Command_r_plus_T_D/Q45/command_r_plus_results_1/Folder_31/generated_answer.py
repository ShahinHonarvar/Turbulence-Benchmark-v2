def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_english_letters = set(s[1:9]).intersection(english_letters)
    palindromes = set()
    for letter in s_english_letters:
        if s.count(letter) >= 3:
            palindromes.add(letter * 3)
        if s.count(letter) >= 5:
            palindromes.add(letter * 5)
    return palindromes