def insert_after_character(text):
    output = ''
    for i, char in enumerate(text):
        if char == 'a':
            output += char + '6'
        else:
            output += char
    return output