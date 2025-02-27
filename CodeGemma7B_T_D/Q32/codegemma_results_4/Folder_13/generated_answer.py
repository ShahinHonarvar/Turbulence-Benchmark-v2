def insert_after_character(s):
    new_s = ''
    for char in s:
        if char == 'x':
            new_s += char + 'N'
        else:
            new_s += char
    return new_s