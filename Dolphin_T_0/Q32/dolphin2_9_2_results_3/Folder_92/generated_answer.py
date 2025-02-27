def insert_after_character(s):
    new_s = ''
    for char in s:
        new_s += char
        if char == 'a':
            new_s += 'a'
    return new_s