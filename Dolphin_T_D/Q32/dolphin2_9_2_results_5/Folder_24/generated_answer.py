def insert_after_character(s):
    result = ''
    for ch in s:
        result += ch
        if ch == '0':
            result += '4'
    return result