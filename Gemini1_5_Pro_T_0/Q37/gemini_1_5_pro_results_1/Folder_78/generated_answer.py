def filter_chars(s):
    filtered_chars = ''
    for i in range(75, 100):
        if i < len(s) and '8' <= s[i] <= 'e':
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result