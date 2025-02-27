def filter_chars(s):
    filter_zone = set()
    for i in range(52, 76):
        if i < len(s) and '5' < s[i] < 'f':
            filter_zone.add(s[i])
    return ''.join((c for c in s if c not in filter_zone))