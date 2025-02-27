def insert_before_character(text):
    result = ''
    for char in text:
        if char == 's' and result:
            result += 'w'
        result += char
    return result