def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == ' ':
            result.append('W')
    return ''.join(result)