def insert_after_character(s):
    new_s = ''
    for i in s:
        new_s += i
        if i == 'o':
            new_s += 'O'
    return new_s