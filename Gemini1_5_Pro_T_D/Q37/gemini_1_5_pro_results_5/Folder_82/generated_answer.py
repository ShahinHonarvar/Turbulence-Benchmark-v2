def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 12 <= i <= 25 and 'P' <= s[i] <= 'x':
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result