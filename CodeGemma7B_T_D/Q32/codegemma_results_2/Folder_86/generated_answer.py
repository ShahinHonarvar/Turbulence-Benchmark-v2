def insert_after_character(a):
    b = a
    for i in range(a.count('O')):
        pos = b.index('O')
        b = b[:pos + 1] + 'Q' + b[pos + 1:]
    return b