def insert_after_character(s):
    result = ''
    for char in s:
        result += char + 'O' if char == 'o' else char
    return result