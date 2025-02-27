def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    letters_between_indices = set(input_string[1:7].lower())
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    if not letters_between_indices.issubset(english_letters):
        return palindromes
    for letter in letters_between_indices:
        if input_string.count(letter) > 1:
            palindromes.add(letter * 2)
    return palindromes