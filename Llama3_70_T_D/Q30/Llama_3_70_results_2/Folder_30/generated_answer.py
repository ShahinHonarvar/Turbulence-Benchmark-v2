def insert_before_character(s):
    result = ''
    for c in s:
        if c == '4':
            result += 'F'
        result += c
    return result