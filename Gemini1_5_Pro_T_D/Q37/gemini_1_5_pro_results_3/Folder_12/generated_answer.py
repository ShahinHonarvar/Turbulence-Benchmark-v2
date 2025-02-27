def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i >= 19 and i <= 90 and (s[i] >= 'F') and (s[i] <= 'h'):
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result