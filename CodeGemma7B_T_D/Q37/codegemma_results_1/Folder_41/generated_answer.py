def filter_chars(s):
    new_s = []
    index = 26
    while index <= 64:
        new_s.append(s[index])
        index += 1
    return ''.join(filter(lambda c: c not in ''.join(new_s), s))