def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i >= 19 and i <= 92 and (s[i] >= '8') and (s[i] <= 'm'):
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result