def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'I':
            result += 'i'
        result += c
    return result