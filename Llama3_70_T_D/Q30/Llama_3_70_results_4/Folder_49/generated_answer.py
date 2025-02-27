def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'i':
            result += 'i' + char
        else:
            result += char
    return result