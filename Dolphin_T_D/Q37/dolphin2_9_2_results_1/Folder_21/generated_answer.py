def filter_chars(string):
    for character in range(603, 760):
        if 'Q' <= string[character] <= 'h':
            string = string[:character] + string[character + 1:]
    return string