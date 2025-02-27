def insert_before_character(s):
    res = ''
    for char in s:
        if char == 's':
            res += 'w' + char
        else:
            res += char
    return res