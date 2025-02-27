def insert_after_character(s):
    new_str = ''
    for char in s:
        new_str += char
        if char == 'B':
            new_str += 'N'
    return new_str