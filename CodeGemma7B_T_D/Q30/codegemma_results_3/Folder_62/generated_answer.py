def insert_before_character(s):
    result = ''
    for char in s:
        if char == ' ':
            result += 'o '
        else:
            result += char
    return result