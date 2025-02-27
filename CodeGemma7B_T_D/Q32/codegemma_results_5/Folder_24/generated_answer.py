def insert_after_character(text):
    lst = list(text)
    for i in range(len(lst)):
        if lst[i] == '0':
            lst.insert(i + 1, '4')
    return ''.join(lst)