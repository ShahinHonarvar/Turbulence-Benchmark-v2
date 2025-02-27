def filter_chars(input_string):
    result = ''
    for i in range(1, 8):
        char = input_string[i]
        if 'L' <= char <= 'a':
            continue
        result += char
    return result