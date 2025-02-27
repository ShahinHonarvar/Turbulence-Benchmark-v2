def insert_after_character(text):
    output = ''
    for char in text:
        if char == 'C':
            output += char + 'Z'
        else:
            output += char
    return output