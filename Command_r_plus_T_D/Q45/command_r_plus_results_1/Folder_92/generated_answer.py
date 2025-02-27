def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[4:8].lower()
    letter_set = set(substring)
    intersection = letter_set.intersection(english_letters)
    for letter in intersection:
        if substring.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes