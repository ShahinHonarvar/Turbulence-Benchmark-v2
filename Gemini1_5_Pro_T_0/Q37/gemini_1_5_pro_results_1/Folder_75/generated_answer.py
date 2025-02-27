def filter_chars(s):
    filtered_chars = ''
    for i in range(34, 68):
        if i < len(s) and 'W' <= s[i] <= 'x':
            filtered_chars += s[i]
    result = ''
    for char in s:
        if char not in filtered_chars:
            result += char
    return result