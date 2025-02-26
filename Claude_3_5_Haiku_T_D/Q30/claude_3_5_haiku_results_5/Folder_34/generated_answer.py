def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'A':
            result += 'a'
        result += char
    return result