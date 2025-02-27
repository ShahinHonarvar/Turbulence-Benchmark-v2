def filter_chars(string):
    new_string = []
    for i in range(len(string)):
        if ord(string[i]) >= 32 and ord(string[i]) <= 69:
            if not (ord(string[i]) > ord('B') and ord(string[i]) < ord('v')):
                new_string.append(string[i])
    return ''.join(new_string)