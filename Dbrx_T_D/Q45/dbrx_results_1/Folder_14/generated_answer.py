def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[4:6]
    letters_in_substr = set(substr) & english_letters
    palindromes = {letter * 3 for letter in letters_in_substr}
    return {p for p in palindromes if substr.lower().count(p.lower()) == 3}