def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i < 77 or i >= 87:
            result += string[i]
    for i in range(len(string)):
        if string[i] not in list(';,:'):
            result += string[i]
    return result