def insert_after_character(s):
    new_s = ''
    for i in s:
        new_s += i
        if i == 'U':
            new_s += 'u'
    return new_s