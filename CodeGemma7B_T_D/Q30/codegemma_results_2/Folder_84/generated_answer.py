def insert_before_character(word):
    updated_word = ''
    for char in word:
        if char == 'H':
            updated_word += 'n' + char
        else:
            updated_word += char
    return updated_word