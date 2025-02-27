def filter_chars(string):
    for i in range(len(string)):
        if 19 <= i <= 92 and '8' <= string[i] <= 'm':
            string = string.replace(string[i], '')
    return string