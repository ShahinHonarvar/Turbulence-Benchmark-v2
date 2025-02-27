def filter_chars(s):
    filtered_indices = set()
    filtered_chars = set()
    for i in range(57, 97):
        if '<' <= s[i] <= 'w':
            filtered_chars.add(s[i])
    return ''.join((c for i, c in enumerate(s) if c not in filtered_chars or i < 57 or i > 96))