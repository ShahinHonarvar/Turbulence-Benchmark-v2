def insert_after_character(s):
    s1 = ''
    for i in s:
        s1 += i
        if i == 'A':
            s1 += 'H'
    return s1