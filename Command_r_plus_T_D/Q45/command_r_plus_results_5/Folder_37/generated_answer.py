def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    chars_between_indices = set(s[1:5].lower())
    palindromes = set()
    for char in chars_between_indices:
        if char in english_letters:
            if s[1:5].count(char) >= 2:
                palindromes.add(char * 2)
            if s[1:5].count(char) >= 3:
                palindromes.add(char * 3)
            if s[1:5].count(char) >= 4:
                palindromes.add(char * 4)
    return palindromes