def insert_after_character(str):
    string_to_return = ''
    for i in range(len(str)):
        if str[i] == 'a':
            string_to_return += str[i] + 'A'
        else:
            string_to_return += str[i]
    return string_to_return