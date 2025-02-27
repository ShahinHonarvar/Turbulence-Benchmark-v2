def filter_chars(str):
    for i in range(45, 57):
        if i in range(int(ord('F')), int(ord('n'))):
            str = str.replace(char(i), '')
    return str