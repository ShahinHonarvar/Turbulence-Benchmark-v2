def insert_after_character(text):
    output = ''
    for char in text:
        output += char
        if char == ' ':
            output += 'H'
    return output