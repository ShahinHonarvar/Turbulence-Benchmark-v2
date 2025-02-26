def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'A':
            result += 'H' + char
        else:
            result += char
    return result