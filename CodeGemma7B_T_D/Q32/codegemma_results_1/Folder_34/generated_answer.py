def insert_after_character(str):
    c = 'a'
    for i in str:
        if i == 'A':
            str = str[:str.index(i)] + c + str[str.index(i):]
    return str