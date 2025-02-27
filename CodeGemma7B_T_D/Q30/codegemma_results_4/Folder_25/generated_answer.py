def insert_before_character(a):
    for i in range(len(a)):
        if a[i] == 'e':
            a = a[:i] + 'W' + a[i:]
    return a