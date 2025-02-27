def filter_chars(string):
    for i in range(373, 902):
        if string[i] >= 'T' and string[i] <= 'h':
            string = string[:i] + string[i + 1:]
    return string