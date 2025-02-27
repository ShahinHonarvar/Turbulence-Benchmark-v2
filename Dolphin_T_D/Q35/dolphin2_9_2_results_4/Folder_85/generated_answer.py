def remove_repeat_chars(s):
    chars = ''
    for i in s:
        if s.count(i) == 1 or s.index(i) < 2 or s.index(i) > 7:
            chars += i
    return chars