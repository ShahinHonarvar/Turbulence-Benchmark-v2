def filter_chars(s):
    filtered_chars = set()
    for idx in range(20, min(63, len(s))):
        if 'i' <= s[idx] <= 'k':
            filtered_chars.add(s[idx])
    return ''.join((c for c in s if c not in filtered_chars))