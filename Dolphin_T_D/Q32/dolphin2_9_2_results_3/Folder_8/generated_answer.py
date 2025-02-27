def insert_after_character(text):
    result = ''
    for char in text:
        result += char + 'T' if char == 'E' else char
    return result