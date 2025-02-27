def filter_chars(s):
    filtered_chars = set()
    for i in range(379, 899):
        if 'M' <= s[i] <= 'v':
            filtered_chars.add(s[i])
    for char in filtered_chars:
        s = s.replace(char, '')
    return s