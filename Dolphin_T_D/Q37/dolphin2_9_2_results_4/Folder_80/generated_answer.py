def filter_chars(string):
    for char in range(36, 80):
        if 'a' <= string[char] <= 'i':
            string = string.replace(string[char], '')
    return string