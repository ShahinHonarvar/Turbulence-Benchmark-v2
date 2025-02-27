def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'A':
            result += 'H' + c
        else:
            result += c
    return result