def insert_before_character(string):
    for i in range(len(string)):
        if string[i] == 'm':
            return string[:i] + 'N' + string[i:]
    return string