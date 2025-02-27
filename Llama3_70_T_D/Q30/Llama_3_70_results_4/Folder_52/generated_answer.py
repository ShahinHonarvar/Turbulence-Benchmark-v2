def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'T':
            result += 'V' + char
        else:
            result += char
    return result