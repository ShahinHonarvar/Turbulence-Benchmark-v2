def filter_chars(s):
    to_remove = set()
    for i in range(38, min(100, len(s))):
        if 'A' <= s[i] <= 'Q':
            to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in to_remove))