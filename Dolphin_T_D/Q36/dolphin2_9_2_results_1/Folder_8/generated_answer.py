def filter_chars(string):
    for char in range(82, 93):
        if string[char] > '!' and string[char] < '*':
            string = string.replace(string[char], '')
    return string