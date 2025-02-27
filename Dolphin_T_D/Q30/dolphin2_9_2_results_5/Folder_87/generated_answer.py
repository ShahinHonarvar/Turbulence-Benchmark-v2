def insert_before_character(string):
    output = ''
    for i in range(len(string)):
        if string[i] == 'm':
            output += 'N'
        output += string[i]
    return output