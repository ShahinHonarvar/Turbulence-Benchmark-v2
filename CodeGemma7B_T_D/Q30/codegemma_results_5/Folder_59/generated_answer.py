def insert_before_character(str):
    temp = ''
    for i in str:
        if i in 'o':
            temp += '0' + i
        else:
            temp += i
    return temp