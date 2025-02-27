def filter_chars(s):
    to_remove = [c for c in s[11:73] if 'i' <= c <= 'v']
    return ''.join([char for char in s if char not in to_remove])