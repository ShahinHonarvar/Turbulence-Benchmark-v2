def palindromes_between_indices(text):
    all_possibles = set()
    for first_index in range(6, 10):
        for second_index in range(first_index + 1, 10):
            for third_index in range(second_index + 1, 10):
                first_char, second_char, third_char = (text[first_index], text[second_index], text[third_index])
                first_char_lowercase = first_char.lower()
                second_char_lowercase = second_char.lower()
                third_char_lowercase = third_char.lower()
                potential_palindrome = f'{third_char_lowercase}{second_char_lowercase}{first_char_lowercase}'
                all_possibles.add(potential_palindrome)
    lowercased_text = text.lower()
    possible_answers = set()
    for palindrome in all_possibles:
        if palindrome in lowercased_text:
            possible_answers.add(palindrome)
    return possible_answers