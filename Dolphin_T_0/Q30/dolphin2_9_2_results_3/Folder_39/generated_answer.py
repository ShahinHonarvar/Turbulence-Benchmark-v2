def insert_before_character(text):
    result = ''
    for c in text:
        if c == 'm':
            result += 'Q' + c
        else:
            result += c
    return result