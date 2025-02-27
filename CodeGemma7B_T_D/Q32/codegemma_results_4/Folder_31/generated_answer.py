def insert_after_character(word):
    new_word = ''
    for letter in word:
        if letter == 'B':
            new_word += letter + 'N'
        else:
            new_word += letter
    return new_word