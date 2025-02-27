def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i < 35 or i > 89:
            result += string[i]
        elif string[i] >= 'E' and string[i] <= 't':
            pass
        else:
            result += string[i]
    return result