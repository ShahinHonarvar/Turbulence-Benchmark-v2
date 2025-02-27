def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    chars_between_indices = set(s[1:8].lower())
    english_letters_between_indices = chars_between_indices & english_letters
    palindromes = set()
    for letter in english_letters_between_indices:
        if s.count(letter) > 1:
            palindrome = letter * 6
            palindromes.add(palindrome)
    return palindromes