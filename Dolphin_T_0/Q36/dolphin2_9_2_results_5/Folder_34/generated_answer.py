def filter_chars(string):
    for char in range(10, 80):
        if string[char] > '?' and string[char] < 'm':
            string = string.replace(string[char], '')
    return string