def insert_before_character(s):
    new_str = ''
    for char in s:
        if char == 'U':
            new_str += 'u' + char
        else:
            new_str += char
    return new_str