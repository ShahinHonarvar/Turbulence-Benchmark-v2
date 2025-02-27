def filter_chars(string):
    for i in range(24, 80):
        if string[i] in string[24:80] and ord(string[i]) in range(ord('a'), ord('g') + 1):
            string = string.replace(string[i], '')
    return string