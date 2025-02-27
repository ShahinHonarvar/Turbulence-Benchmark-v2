def filter_chars(s):
    if len(s) < 86:
        return s
    filtered_indices = []
    for i in range(86, min(93, len(s))):
        if '!' <= s[i] <= 's':
            filtered_indices.append(s[i])
    for char in filtered_indices:
        s = s.replace(char, '')
    return s