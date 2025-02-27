def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_english_letters = set(s[1:6]).intersection(english_letters)
    palindromes = set()
    for letter in s_english_letters:
        if s.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes