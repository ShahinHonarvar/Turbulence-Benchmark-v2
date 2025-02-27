def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'C':
            result += 'H'
        result += c
    return result