def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'P':
            result += 'V'
        result += c
    return result