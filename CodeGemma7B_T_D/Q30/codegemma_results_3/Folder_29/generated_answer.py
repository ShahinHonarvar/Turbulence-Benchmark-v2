def insert_before_character(text):
    new_str = ''
    for char in text:
        if char == 'N':
            new_str += 'z' + char
        else:
            new_str += char
    return new_str