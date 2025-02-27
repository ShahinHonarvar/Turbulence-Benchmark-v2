def insert_after_character(s):
    new_s = ''
    for char in s:
        new_s += char
        if char == '9':
            new_s += 'M'
    return new_s