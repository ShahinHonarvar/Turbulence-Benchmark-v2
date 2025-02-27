def insert_after_character(s):
    result = ''
    for c in s:
        if c == 'u':
            result += 'u'
        result += c
    return result