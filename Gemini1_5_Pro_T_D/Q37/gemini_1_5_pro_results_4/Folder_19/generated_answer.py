def filter_chars(s):
    filtered_chars = ''
    for i in range(35, 90):
        if i < len(s) and 'E' <= s[i] <= 't':
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result