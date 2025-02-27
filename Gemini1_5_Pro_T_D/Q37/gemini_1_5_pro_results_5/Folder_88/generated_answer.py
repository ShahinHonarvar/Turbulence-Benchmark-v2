def filter_chars(s):
    filtered_chars = ''
    for i in range(69, 81):
        if i < len(s) and s[i] >= '@' and (s[i] <= 'p'):
            filtered_chars += s[i]
    result = ''
    for char in s:
        if char not in filtered_chars:
            result += char
    return result