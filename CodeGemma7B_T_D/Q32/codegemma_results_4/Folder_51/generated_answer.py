def insert_after_character(s):
    new_s = ''
    for char in s:
        if char == 'o':
            new_s += char + 'O'
        else:
            new_s += char
    return new_s