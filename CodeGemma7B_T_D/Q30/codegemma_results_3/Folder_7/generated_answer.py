def insert_before_character(string):
    for i in range(len(string)):
        if string[i] == ' ':
            string = string[:i] + 'H' + string[i:]
    return string