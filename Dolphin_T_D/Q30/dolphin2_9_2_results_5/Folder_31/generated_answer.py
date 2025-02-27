def insert_before_character(s):
    res = ''
    for char in s:
        if char == 'B':
            res += 'N' + char
        else:
            res += char
    return res