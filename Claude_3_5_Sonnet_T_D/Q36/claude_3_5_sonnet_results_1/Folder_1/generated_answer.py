def filter_chars(s):
    filtered_chars = set()
    for i in range(70, 87):
        if i < len(s) and '#' < s[i] < 'L':
            filtered_chars.add(s[i])
    return ''.join((c for c in s if c not in filtered_chars))