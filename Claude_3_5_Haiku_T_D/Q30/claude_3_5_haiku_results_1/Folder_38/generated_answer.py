def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'X':
            result += '6'
        result += char
    return result