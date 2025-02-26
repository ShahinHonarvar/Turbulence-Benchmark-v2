def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'A':
            result += 'A'
        result += char
    return result