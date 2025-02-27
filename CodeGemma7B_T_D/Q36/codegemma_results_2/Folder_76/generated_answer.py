def filter_chars(string):
    for i in range(669, 888):
        if string[i] > 'B' and string[i] < 'Y':
            for j in range(i, len(string)):
                if string[j] == string[i]:
                    string = string[:j] + string[j + 1:]
    return string