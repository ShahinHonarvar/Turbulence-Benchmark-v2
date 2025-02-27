def filter_chars(string):
    for i in range(379, 899):
        if ord(string[i]) >= ord('M') and ord(string[i]) <= ord('v'):
            string = string[:i] + string[i + 1:]
    return string