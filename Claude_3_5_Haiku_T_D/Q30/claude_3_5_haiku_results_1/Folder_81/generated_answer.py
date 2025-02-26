def insert_before_character(s):
    result = []
    for char in s:
        if char == 'A':
            result.append('A')
        result.append(char)
    return ''.join(result)