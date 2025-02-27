def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'a':
            result += 't'
        result += c
    return result