def remove_repeat_chars(s):
    return ''.join((x for x in s if s.index(x) not in range(10, 76)))