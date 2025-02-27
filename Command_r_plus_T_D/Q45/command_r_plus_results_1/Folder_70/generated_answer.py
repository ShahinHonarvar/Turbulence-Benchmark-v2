def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[1:7])
    palindromes = set()
    for letter in english_letters.intersection(s_letters):
        if s.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes