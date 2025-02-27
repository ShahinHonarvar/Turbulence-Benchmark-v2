def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_between_indices = set(input_string[4:7].lower())
    if letters_between_indices.issubset(english_letters):
        for letter in letters_between_indices:
            if input_string.count(letter) >= 3:
                palindromes.add(letter * 3)
    return palindromes