def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'i':
            result += 'i'
        result += char
    return result