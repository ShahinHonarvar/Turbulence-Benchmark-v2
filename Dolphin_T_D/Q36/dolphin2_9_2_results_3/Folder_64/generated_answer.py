def filter_chars(s):
    to_remove = [s[i] for i in range(1, 7) if '3' < s[i] < '^']
    return ''.join([ch for ch in s if ch not in to_remove])