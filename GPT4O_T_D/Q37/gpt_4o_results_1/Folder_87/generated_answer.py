def filter_chars(s):
    filtered_chars = set()
    for i in range(18, min(82, len(s))):
        if 'W' <= s[i] <= '[':
            filtered_chars.add(s[i])
    return ''.join((c for c in s if c not in filtered_chars))