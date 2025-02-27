def palindromes_between_indices(input_string: str) -> set:
    input_string = input_string.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    char_between_indices = set(input_string[1:9])
    filtered_letters = char_between_indices & english_letters
    palindromes = set()
    for letter in filtered_letters:
        if input_string.count(letter) >= 2:
            palindromes.add(letter * 2)
    for first_letter in filtered_letters:
        for second_letter in filtered_letters:
            if first_letter != second_letter:
                palindromes.add(first_letter + second_letter + second_letter + first_letter)
    return palindromes