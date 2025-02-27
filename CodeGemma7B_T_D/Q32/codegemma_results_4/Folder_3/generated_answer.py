def insert_after_character(word):
    new_word = ''
    for character in word:
        if character == '0':
            new_word += character + 'H'
        else:
            new_word += character
    return new_word