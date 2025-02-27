def insert_after_character(word):
    new_word = ''
    for letter in word:
        if letter == 'O':
            new_word += letter + 'd'
        else:
            new_word += letter
    return new_word