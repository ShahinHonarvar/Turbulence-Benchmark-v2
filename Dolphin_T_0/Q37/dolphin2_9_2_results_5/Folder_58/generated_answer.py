def filter_chars(input_string):
    char_set = set()
    for i in range(503, 754):
        char = input_string[i]
        if '9' <= char <= 'w':
            char_set.add(char)
    return ''.join((c for c in input_string if c not in char_set))