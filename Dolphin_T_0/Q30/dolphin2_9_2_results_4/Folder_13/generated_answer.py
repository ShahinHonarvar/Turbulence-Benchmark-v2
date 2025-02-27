def insert_before_character(s):
    lst = list(s)
    for i in range(len(lst)):
        if lst[i] == 'x':
            lst.insert(i, 'N')
    return ''.join(lst)