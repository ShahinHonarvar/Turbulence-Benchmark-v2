def insert_after_character(s):
    new_string = ''
    for i in s:
        new_string += i + ('o' if i == 'o' else '')
    return new_string