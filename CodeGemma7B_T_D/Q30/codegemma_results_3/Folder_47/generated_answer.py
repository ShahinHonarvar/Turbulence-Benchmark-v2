def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'E':
            result += 'fE'
        else:
            result += char
    return result