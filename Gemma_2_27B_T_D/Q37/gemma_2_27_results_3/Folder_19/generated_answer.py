def filter_chars(s):
    filtered_chars = set()
    for i in range(35, 90):
        if 'E' <= s[i] <= 't':
            filtered_chars.add(s[i])
    result = ''.join([c for c in s if c not in filtered_chars])
    return result