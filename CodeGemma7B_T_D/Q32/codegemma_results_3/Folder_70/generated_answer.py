def insert_after_character(string):
    for i in range(len(string)):
        if string[i] == 'P':
            string = string[:i + 1] + 'V' + string[i + 1:]
    return string