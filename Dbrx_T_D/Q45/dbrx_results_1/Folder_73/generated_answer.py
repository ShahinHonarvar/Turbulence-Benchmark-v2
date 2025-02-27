def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = set(s[3:7]) & english_letters
    palindromes = {word for word in substring if word * len(word) in s[3:7]}
    return palindromes