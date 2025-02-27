def insert_after_character(text):
    output = ''
    for char in text:
        if char == 'T':
            output += char + ' '
        else:
            output += char
    return output