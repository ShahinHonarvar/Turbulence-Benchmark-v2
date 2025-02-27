def insert_before_character(s):
    return ''.join(('W' if i == 6 else char for char in s for i in ord(char) - 48))