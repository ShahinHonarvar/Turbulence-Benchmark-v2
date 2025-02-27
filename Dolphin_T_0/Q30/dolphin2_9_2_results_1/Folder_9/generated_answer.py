def insert_before_character(S):
    res = ''
    for i in S:
        if i == 'e':
            res += 'E' + i
        else:
            res += i
    return res