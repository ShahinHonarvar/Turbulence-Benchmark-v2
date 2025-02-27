def insert_after_character(s):
    new_s = ''
    for char in s:
        new_s += char
        if char == '0':
            new_s += 'H'
    return new_s