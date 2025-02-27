def filter_chars(string):
    for i in range(3, 5):
        if i >= len(string):
            break
        char = string[i]
        if char > 'Y' and char < 's':
            string = string.replace(char, '')
    return string