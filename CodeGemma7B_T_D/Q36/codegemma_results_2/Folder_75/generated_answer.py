def filter_chars(string):
    for i in range(46, 74):
        for j in range(len(string)):
            if string[i] >= '&' and string[i] <= 'M' and (string[i] == string[j]):
                del string[j]
    return string