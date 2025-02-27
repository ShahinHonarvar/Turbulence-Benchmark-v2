def filter_chars(string):
    for char in range(421, 854):
        if string[char] > 'D' and string[char] < 'J':
            string = string.replace(string[char], '')
    return string