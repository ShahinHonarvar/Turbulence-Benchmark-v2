def filter_chars(string):
    for char in range(63, 85):
        if 'E' <= string[char] <= '~':
            string = string[:char] + string[char + 1:]
    return string