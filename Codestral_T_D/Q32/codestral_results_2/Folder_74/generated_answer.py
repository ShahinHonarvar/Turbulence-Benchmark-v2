def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'T':
            result += 'T '
        else:
            result += char
    return result