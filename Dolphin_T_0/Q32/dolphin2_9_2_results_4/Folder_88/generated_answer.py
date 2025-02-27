def insert_after_character(s):
    new_s = ''
    for char in s:
        new_s += char
        if char == 'a':
            new_s += 't'
    return new_s