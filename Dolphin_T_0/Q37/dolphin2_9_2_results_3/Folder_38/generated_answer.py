def filter_chars(string):
    for char in range(24, 80):
        if 'a' <= string[char] <= 'f':
            string = string.replace(string[char], '')
    return string