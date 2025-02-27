def insert_before_character(string):
    for i in range(len(string)):
        if string[i] == 'a':
            string = string[:i] + '6' + string[i:]
    return string