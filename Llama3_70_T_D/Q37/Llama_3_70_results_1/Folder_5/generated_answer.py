def filter_chars(s):
    original_string = s
    for i in range(24, 83):
        if '5' <= original_string[i] <= '<':
            s = s.replace(original_string[i], '')
    return s