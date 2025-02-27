def filter_chars(string):
    for char in range(18, 82):
        if string[char] >= 'W' and string[char] <= '[':
            string = string[:char] + string[char + 1:]
    return string