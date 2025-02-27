def filter_chars(s):
    remove_chars = {s[i] for i in range(47, 74) if '&' < s[i] < 'M'}
    return ''.join((ch for ch in s if ch not in remove_chars))