def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'C':
            result += 'Z' + char
        else:
            result += char
    return result