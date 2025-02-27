def filter_chars(string):
    char_map = {}
    for i, char in enumerate(string):
        if 2 <= i <= 7:
            if 'h' < char < 'k':
                char_map[char] = char_map.get(char, 0) + 1
    for char in char_map:
        string = string.replace(char, '')
    return string