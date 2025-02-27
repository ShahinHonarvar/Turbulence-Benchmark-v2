def insert_before_character(string):
    for i in range(len(string) - 1):
        if string[i] == '2':
            string = string[:i] + 'S' + string[i:]
    return string