def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'K':
            result += ''
        result += char
    if result.endswith('K'):
        result += ''
    return result