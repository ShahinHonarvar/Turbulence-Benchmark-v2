def insert_after_character(mystring):
    result = ''
    for char in mystring:
        result += char + ('X' if char == ' ' else '')
    return result