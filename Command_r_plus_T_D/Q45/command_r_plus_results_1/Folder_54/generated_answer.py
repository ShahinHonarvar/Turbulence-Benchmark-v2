def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[4:10].lower()
    substring_set = set(substring)
    english_letters_in_substring = substring_set.intersection(english_letters)
    for letter in english_letters_in_substring:
        if substring.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes