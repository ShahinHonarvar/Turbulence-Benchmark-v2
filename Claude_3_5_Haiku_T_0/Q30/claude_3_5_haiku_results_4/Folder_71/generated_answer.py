def insert_before_character(text):
    result = ''
    for char in text:
        if char == '2':
            result += 'S2'
        else:
            result += char
    return result