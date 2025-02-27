def insert_before_character(string):
    return ''.join((insert_before_h(char) for char in string))

def insert_before_h(char):
    if char == 'H':
        return 's' + char
    else:
        return char