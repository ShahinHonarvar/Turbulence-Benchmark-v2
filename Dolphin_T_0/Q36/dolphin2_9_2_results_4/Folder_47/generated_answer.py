def filter_chars(s):
    to_remove = [ch for ch in s if 45 <= s.index(ch) < 57 and 'F' < ch < 'n']
    return ''.join([ch for ch in s if ch not in to_remove])