def insert_after_character(text):
    new_string = ''
    for char in text:
        if char == 'c':
            new_string += char + 'G'
        else:
            new_string += char
    return new_string