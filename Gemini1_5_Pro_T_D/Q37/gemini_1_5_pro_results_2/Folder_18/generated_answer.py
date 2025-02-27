def filter_chars(s):
    filtered_chars = ''
    for i in range(770, 971):
        if i < len(s) and '-' <= s[i] <= 'D':
            filtered_chars += s[i]
    for char in filtered_chars:
        s = s.replace(char, '')
    return s