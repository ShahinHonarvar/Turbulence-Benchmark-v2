def insert_after_character(s):
    result = ''
    for c in s:
        if c == 'k':
            result += c + 'k'
        else:
            result += c
    return result