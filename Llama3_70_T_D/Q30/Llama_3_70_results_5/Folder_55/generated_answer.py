def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'u':
            result += 'U'
        result += c
    return result