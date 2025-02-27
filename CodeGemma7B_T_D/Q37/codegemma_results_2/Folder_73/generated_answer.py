def filter_chars(string):
    for i in range(22, 86):
        for j in range(i, len(string)):
            if string[i] == string[j]:
                string = string[:j] + string[j + 1:]
    return string