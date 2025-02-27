def filter_chars(string):
    for i in range(373, 902):
        if 'T' <= string[i] <= 'h':
            string = string[:i] + string[i + 1:]
    return string