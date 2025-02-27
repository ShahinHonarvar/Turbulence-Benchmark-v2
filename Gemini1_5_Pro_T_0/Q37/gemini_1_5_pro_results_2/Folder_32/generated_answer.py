def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 23 <= i <= 89 and 'w' <= s[i] <= '{':
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result