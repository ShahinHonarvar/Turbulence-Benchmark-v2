def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'j':
            result += 'q'
        result += c
    return result