def insert_after_character(a):
    b = ''
    for i in a:
        if i == 'X':
            b += i + 'u'
        else:
            b += i
    return b