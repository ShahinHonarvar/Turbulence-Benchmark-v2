def insert_after_character(s):
    result = ''
    for c in s:
        result += c
        if c == 'j':
            result += 'v'
    return result