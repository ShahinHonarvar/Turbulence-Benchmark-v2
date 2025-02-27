def insert_before_character(word):
    new_word = ''
    for letter in word:
        if letter == 'S':
            new_word += 'U' + letter
        else:
            new_word += letter
    return new_word