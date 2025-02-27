def insert_after_character(s):
    new_s = ''
    for char in s:
        new_s += char
        if char == '6':
            new_s += '9'
    return new_s