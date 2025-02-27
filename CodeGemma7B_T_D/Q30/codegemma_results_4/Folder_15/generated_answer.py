def insert_before_character(str):
    newstr = ''
    for i in str:
        newstr += i
        if i == 'o':
            newstr += 'o'
    return newstr