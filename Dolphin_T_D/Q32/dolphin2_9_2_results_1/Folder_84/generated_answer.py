def insert_after_character(s):
    new_s = ''
    for char in s:
        new_s += char
        if char == 'H':
            new_s += 'n'
    return new_s