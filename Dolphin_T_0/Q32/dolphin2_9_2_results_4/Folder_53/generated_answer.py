def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'i':
            result += char + 'I'
        else:
            result += char
    return result