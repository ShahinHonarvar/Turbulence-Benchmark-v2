def insert_after_character(s):
    new_s = ''
    for i in s:
        new_s += i
        if i == 'C':
            new_s += 'H'
    return new_s