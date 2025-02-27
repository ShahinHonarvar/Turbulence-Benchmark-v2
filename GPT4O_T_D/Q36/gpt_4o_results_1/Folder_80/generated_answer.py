def filter_chars(s):
    s = list(s)
    for i in range(55, 92):
        if 'J' < s[i] < 'X':
            s = [ch for ch in s if ch != s[i]]
    return ''.join(s)