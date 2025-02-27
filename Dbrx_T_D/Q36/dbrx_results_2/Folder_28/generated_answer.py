def filter_chars(s):
    for i in range(31, 73):
        if 'M' < s[i] < 'j':
            while True:
                try:
                    s = s[:i] + s[i + 1:]
                    i -= 1
                except IndexError:
                    break
    return s