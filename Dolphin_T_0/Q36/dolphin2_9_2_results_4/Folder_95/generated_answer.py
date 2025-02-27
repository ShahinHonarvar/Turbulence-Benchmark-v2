def filter_chars(s):
    to_remove = [s[i] for i in range(56, 86) if s[i] > '+' and s[i] < 'w']
    return ''.join([ch for ch in s if ch not in to_remove])