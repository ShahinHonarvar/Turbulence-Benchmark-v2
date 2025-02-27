def insert_before_character(string):
    result = ''
    for c in string:
        if c == 'a':
            result += 'A' + c
        else:
            result += c
    return result