def filter_chars(string):
    for i in range(36, 41):
        for j in range(string.count(string[i])):
            string = string.replace(string[i], '', 1)
    return string