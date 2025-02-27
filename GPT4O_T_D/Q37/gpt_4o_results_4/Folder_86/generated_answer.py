def filter_chars(s):
    filtered_chars = set()
    for i in range(max(164, 0), min(707, len(s))):
        if 'O' <= s[i] <= '}':
            filtered_chars.add(s[i])
    result = ''.join((c for c in s if c not in filtered_chars))
    return result