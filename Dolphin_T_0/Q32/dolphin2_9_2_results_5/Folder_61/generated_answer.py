def insert_after_character(s):
    result = ''
    for ch in s:
        result += ch
        if ch == 'e':
            result += '0'
    return result