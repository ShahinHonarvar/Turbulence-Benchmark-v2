def filter_chars(s):
    s = list(s)
    for i in range(31, 73):
        if 'M' < s[i] < 'j':
            s = [ch for ch in s if ch != s[i]]
    return ''.join(s)