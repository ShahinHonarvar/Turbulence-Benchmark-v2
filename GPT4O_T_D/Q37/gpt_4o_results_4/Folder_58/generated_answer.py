def filter_chars(s):
    if len(s) < 504:
        return s
    filter_set = set()
    for i in range(503, min(754, len(s))):
        if '9' <= s[i] <= 'w':
            filter_set.add(s[i])
    return ''.join([ch for ch in s if ch not in filter_set])