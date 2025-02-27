def filter_chars(s):
    to_remove = [s[i] for i in range(46, 74) if '&' < s[i] < 'M']
    return ''.join((ch for ch in s if ch not in to_remove))