def insert_after_character(s):
    new_str = []
    for char in s:
        if char == 'w':
            new_str.append(char)
            new_str.append('n')
        else:
            new_str.append(char)
    return ''.join(new_str)