def insert_after_character(string):
    for i in range(len(string)):
        if string[i] == ' ':
            string = string[:i + 1] + 'W' + string[i + 1:]
    return string