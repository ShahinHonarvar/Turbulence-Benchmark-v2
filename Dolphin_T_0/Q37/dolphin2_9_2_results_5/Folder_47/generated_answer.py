def filter_chars(string):
    for char in range(38, 55):
        if ':' <= string[char] <= 'r':
            string = string.replace(string[char], '')
    return string