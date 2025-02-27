def insert_before_character(text):
    result = ''
    for ch in text:
        if ch == 'F':
            result += 'u' + ch
        else:
            result += ch
    return result