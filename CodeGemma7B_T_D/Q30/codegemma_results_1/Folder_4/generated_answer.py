def insert_before_character(str):
    new_str = []
    for char in str:
        if char == 'a':
            new_str.append('6')
        new_str.append(char)
    return ''.join(new_str)