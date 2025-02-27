def insert_after_character(s):
    new_str = ''
    for i in s:
        new_str += i
        if i == '6':
            new_str += 'W'
    return new_str