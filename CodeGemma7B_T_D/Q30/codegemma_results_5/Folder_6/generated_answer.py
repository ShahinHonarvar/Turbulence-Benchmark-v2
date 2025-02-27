def insert_before_character(word):
    new_word = ''
    for char in word:
        if char == 'X':
            new_word += 'uX'
        else:
            new_word += char
    return new_word