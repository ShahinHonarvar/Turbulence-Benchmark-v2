def insert_after_character(s):
    """Inserts character 'i' immediately succeeding any occurrences of character 'I' in a string"""
    new_string = ''
    for char in s:
        if char == 'I':
            new_string += char + 'i'
        else:
            new_string += char
    return new_string