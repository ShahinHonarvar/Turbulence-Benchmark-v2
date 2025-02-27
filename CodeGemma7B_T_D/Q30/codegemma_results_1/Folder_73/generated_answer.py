def insert_before_character(string):
    for i in range(len(string)):
        if string[i] == 'R':
            string = string[:i] + 'V' + string[i:]
    return string