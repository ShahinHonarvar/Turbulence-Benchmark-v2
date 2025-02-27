def insert_before_character(str):
    new_str = []
    for char in str:
        if char == 'u':
            new_str.append('U')
        new_str.append(char)
    return ''.join(new_str)