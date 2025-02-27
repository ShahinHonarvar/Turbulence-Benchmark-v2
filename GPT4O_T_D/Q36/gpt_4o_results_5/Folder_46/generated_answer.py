def filter_chars(s):
    to_filter = set()
    for i in range(20, 69):
        if i < len(s) and '<' < s[i] < 'C':
            to_filter.add(s[i])
    return ''.join((c for c in s if c not in to_filter))