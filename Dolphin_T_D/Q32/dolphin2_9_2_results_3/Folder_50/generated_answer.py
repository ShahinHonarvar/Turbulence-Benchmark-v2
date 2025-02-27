def insert_after_character(s):
    new_str = ''
    for i in s:
        new_str += i
        if i == 't':
            new_str += 'u'
    return new_str