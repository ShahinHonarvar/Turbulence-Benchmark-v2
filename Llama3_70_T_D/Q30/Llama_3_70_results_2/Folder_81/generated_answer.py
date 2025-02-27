def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'A':
            result += 'A'
        result += c
    return result