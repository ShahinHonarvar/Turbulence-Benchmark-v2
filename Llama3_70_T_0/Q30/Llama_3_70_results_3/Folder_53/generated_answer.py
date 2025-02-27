def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'i':
            result += 'I'
        result += char
    return result