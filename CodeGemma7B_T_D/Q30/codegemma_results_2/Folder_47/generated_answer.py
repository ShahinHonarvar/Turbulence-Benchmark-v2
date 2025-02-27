def insert_before_character(s):
    new_str = ''
    for char in s:
        if char == 'E':
            new_str += 'fE'
        else:
            new_str += char
    return new_str