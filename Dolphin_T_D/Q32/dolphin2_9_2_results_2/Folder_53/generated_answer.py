def insert_after_character(s):
    res = ''
    for char in s:
        res += char
        if char == 'i':
            res += 'I'
    return res