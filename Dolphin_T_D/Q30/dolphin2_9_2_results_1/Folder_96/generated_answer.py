def insert_before_character(string):
    result = ''
    for char in string:
        if char.lower() == 'a':
            result += 'A' + char
        else:
            result += char
    return result