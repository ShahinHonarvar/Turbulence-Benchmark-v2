def insert_before_character(string):
    result = ''
    for i in range(len(string)):
        if string[i] == 'C':
            result += 'H' + string[i]
        else:
            result += string[i]
    return result