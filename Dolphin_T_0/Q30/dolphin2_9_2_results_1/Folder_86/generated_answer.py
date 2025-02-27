def insert_before_character(s):
    new_s = ''
    for char in s:
        if char == 'O':
            new_s += 'Q' + char
        else:
            new_s += char
    return new_s