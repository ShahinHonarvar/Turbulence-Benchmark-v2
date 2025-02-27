def filter_chars(s):
    filtered_chars = set()
    for i in range(27, min(86, len(s))):
        if 'c' <= s[i] <= 'i':
            filtered_chars.add(s[i])
    return ''.join((ch for ch in s if ch not in filtered_chars))