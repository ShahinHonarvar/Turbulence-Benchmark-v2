def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'e':
            result += 'E' + char
        else:
            result += char
    return result