def insert_after_character(s):
    new_s = ''
    for i in s:
        new_s += i
        if i == 'r':
            new_s += 'w'
    return new_s