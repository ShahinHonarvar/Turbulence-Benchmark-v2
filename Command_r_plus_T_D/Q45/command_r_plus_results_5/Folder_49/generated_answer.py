def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    substring = s[5:8].lower()
    substring_set = set(substring)
    for letter in substring_set:
        if substring.count(letter) > 1:
            palindromes.add(letter * 3)
    return palindromes