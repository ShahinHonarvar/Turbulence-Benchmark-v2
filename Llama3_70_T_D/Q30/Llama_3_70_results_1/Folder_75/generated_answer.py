def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'U':
            result += 'q' + char
        else:
            result += char
    return result