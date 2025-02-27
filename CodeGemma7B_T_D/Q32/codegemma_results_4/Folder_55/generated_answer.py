def insert_after_character(str1):
    return ''.join(['U' + char if char == 'u' else char for char in str1])