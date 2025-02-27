def insert_before_character(s):
    new_s = ''
    for char in s:
        if char == 'i':
            new_s += 'I' + char
        else:
            new_s += char
    return new_s