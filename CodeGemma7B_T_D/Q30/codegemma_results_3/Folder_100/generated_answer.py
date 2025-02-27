def insert_before_character(str):
    out = ''
    for char in str:
        if char == '0':
            out += ' ' + char
        else:
            out += char
    return out