def insert_before_character(s):
    result = ''
    for char in s:
        if char == ' ':
            result += 'o'
        result += char
    return result