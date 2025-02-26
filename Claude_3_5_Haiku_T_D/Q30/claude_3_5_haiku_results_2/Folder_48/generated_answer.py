def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'S':
            result += 'U'
        result += char
    return result