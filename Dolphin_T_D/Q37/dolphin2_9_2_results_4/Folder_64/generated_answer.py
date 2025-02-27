def filter_chars(input_str):
    c = ''
    for char in input_str:
        if 1 <= input_str.index(char) <= 7 and 'L' <= char <= 'a':
            continue
        else:
            c += char
    return c