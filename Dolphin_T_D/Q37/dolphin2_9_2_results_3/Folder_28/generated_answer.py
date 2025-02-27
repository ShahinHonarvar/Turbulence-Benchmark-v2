def filter_chars(s):
    to_filter = set(s[20:80])
    filtered = [ch for ch in s if ch not in to_filter]
    return ''.join(filtered)