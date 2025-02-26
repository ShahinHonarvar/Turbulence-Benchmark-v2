def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'C':
            result += 'Z'
        result += char
    return result