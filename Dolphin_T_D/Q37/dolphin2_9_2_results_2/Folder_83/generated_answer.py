def filter_chars(s):
    to_remove = [c for c in s[29:80] if 'K' <= c <= 'z']
    return ''.join([ch for ch in s if ch not in to_remove])