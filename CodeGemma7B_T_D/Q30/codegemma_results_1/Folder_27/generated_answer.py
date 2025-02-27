def insert_before_character(string):
    for i in range(len(string)):
        if string[i] == 'N':
            return string[:i] + 'j' + string[i:]
    return string + 'j'