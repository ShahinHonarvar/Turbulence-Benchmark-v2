def palindromes_between_indices(text):
    english_letters = set(string.ascii_lowercase + string.ascii_uppercase)
    current_letter_index = 0
    palindromes = set()
    for index, letter in enumerate(text):
        current_letter_index += 1
        if current_letter_index < 7:
            continue
        if letter in english_letters and index >= 6:
            current_word = text[index - 6:index + 1]
            current_word = ''.join(sorted(current_word))
            if current_word not in palindromes:
                palindromes.add(current_word)
    return palindromes