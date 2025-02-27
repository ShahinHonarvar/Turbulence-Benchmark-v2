def insert_after_character(s):
    c = 'c'
    g = 'G'
    new_str = ''
    for char in s:
        new_str += char
        if char == c:
            new_str += g
    return new_str