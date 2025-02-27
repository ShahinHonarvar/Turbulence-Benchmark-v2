def insert_after_character(text):
    new_string = ''
    for char in text:
        if char == 'o':
            new_string += char + 'a'
        else:
            new_string += char
    return new_string