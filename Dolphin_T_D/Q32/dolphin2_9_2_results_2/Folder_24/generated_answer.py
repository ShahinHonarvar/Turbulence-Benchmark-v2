def insert_after_character(string):
    modified_str = ''
    for i in range(len(string)):
        modified_str += string[i]
        if string[i] == '0':
            modified_str += '4'
    return modified_str