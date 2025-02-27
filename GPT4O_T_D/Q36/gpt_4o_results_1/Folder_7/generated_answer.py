def filter_chars(s):
    filtered_indices = set()
    for i in range(503, 946):
        if 'W' < s[i] < 'y':
            filtered_indices.add(s[i])
    return ''.join((c for c in s if c not in filtered_indices))