def insert_after_character(s):
    new_s = ''
    for char in s:
        if char == 'a':
            new_s += char + 'W'
        else:
            new_s += char
    return new_s