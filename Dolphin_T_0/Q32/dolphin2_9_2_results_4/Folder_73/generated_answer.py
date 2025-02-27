def insert_after_character(s):
    new_str = ''
    for i in s:
        new_str += i
        if i == 'R':
            new_str += 'V'
    return new_str