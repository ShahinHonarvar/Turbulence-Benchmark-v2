def filter_chars(s):
    new_s = []
    for i, char in enumerate(s):
        if not (124 <= i <= 854 and '9' <= char <= 's'):
            new_s.append(char)
    return ''.join(new_s)