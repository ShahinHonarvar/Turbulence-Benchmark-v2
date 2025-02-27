def insert_after_character(str1):
    new_str = ''
    for char in str1:
        if char == ' ':
            char += '5'
        new_str += char
    return new_str