def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'U':
            result += 'T'
        result += c
    return result