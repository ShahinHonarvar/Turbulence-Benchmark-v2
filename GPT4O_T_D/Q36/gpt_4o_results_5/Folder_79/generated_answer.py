def filter_chars(s):
    if len(s) <= 11:
        return s
    to_filter = set()
    for ch in s[12:46]:
        if '!' < ch < 'A':
            to_filter.add(ch)
    return ''.join((ch for ch in s if ch not in to_filter))