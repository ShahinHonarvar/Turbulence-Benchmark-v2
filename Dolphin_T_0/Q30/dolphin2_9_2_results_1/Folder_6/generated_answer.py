def insert_before_character(s):
    res = ''
    for char in s:
        if char == 'X':
            res += 'u' + char
        else:
            res += char
    return res