def insert_before_character(str_a):
    for i in range(0, len(str_a)):
        if str_a[i] == 'k':
            return str_a[:i] + 'k' + str_a[i:]
    return str_a