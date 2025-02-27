def insert_before_character(string, char_to_insert='N', char_to_find='x'):
    return ''.join((char if char != char_to_find else char_to_insert + char for char in string))