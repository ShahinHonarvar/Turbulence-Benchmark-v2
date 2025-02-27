def insert_before_character(s):
    result = ''
    for char in s:
        if char == ' ':
            result += 'K '
        else:
            result += char
    return result