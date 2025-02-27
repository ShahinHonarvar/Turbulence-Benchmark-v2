def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i >= 17 and i <= 63 and (s[i] >= 'O') and (s[i] <= '^'):
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result