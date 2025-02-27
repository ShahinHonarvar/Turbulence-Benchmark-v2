def insert_after_character(word):
    new_word = ''
    for char in word:
        if char == '2':
            new_word += char + 'S'
        else:
            new_word += char
    return new_word