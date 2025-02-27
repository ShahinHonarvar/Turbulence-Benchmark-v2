def insert_after_character(s):
    new_s = ''
    for char in s:
        if char == '0':
            new_s += char + ' '
        else:
            new_s += char
    return new_s