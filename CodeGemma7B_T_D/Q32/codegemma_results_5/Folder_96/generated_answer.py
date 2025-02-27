def insert_after_character(string):
    s2 = ''
    for i in range(len(string)):
        s2 += string[i]
        if string[i] == 'a':
            s2 += 'A'
    return s2