def insert_after_character(string):
    for i in range(len(string)):
        if string[i] == 'E':
            string = string[:i + 1] + 'e' + string[i + 1:]
    return string