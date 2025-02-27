def filter_chars(string):
    for char in range(86, 93):
        if string[char] > 'E' and string[char] < '~':
            string = string[:char] + string[char + 1:]
    return string