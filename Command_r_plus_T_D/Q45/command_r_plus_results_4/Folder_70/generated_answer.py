def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    chars_between_indices = set(s[1:7].lower())
    english_letters_between_indices = chars_between_indices & english_letters
    if len(english_letters_between_indices) < 2:
        return set()
    palindromes = set()
    for char in english_letters_between_indices:
        if s[1:7].lower().count(char) >= 2:
            palindromes.add(char * 2)
    return palindromes