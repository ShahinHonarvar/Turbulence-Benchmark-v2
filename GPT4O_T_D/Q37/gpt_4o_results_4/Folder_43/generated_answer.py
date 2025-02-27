def filter_chars(s):
    to_remove = set()
    for i in range(min(len(s), 56)):
        if 15 <= i <= 55 and 'W' <= s[i] <= '{':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))