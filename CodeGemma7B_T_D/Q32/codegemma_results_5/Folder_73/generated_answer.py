def insert_after_character(text):
    output = ''
    for char in text:
        if char == 'R':
            output += char + 'V'
        else:
            output += char
    return output