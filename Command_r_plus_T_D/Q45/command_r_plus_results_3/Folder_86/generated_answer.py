def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_in_range = set(s[6:10].lower()) & english_letters
    palindromes = set()
    for letter in letters_in_range:
        if s[6:10].lower().count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes