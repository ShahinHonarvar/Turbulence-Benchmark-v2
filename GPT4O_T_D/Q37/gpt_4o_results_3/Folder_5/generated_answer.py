def filter_chars(s):
    filtered = set()
    for c in s[24:83]:
        if '5' <= c <= '<':
            filtered.add(c)
    return ''.join((c for c in s if c not in filtered))