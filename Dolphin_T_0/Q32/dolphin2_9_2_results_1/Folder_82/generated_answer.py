def insert_after_character(string):
    result = ''
    for char in string:
        result += char + ('I' if char == 'I' else '')
    return result