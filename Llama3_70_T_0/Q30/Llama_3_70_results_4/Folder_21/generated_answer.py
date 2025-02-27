def insert_before_character(s):
    result = ''
    for char in s:
        if char == ' ':
            result += 'K'
        result += char
    return result