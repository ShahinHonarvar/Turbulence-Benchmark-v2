def filter_chars(string):
    for i in range(len(string)):
        if 33 <= i <= 70 and ord(string[i]) >= ord('7') and (ord(string[i]) <= ord('k')):
            while string.count(string[i]) > 0:
                string = string.replace(string[i], '')
    return string