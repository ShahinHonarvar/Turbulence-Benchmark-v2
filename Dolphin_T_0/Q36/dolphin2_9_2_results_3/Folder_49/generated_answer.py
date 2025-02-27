def filter_chars(string):
    for i in range(46, 91):
        for j in range(len(string)):
            if string[j] == string[i] and string[j] > 'D' and (string[j] < 'H'):
                string = string[:j] + string[j + 1:]
    return string