def filter_chars(s):
    to_remove = [c for c in s[384:412] if '/' <= c <= '8']
    return ''.join((ch for ch in s if ch not in to_remove))