def insert_after_character(str):
    a = list(str)
    for i in range(len(a)):
        if a[i] == 'S' and a[i + 1] != 'U':
            a[i + 1] = 'U'
    s = ''.join(a)
    return s