def insert_before_character(text):
    result = ''
    for char in text:
        if char == '5':
            result += 'R' + char
        else:
            result += char
    return result