def insert_before_character(d):
    a = ''
    for i in d:
        if i == 'Y':
            a = a + '4' + i
        else:
            a = a + i
    return a