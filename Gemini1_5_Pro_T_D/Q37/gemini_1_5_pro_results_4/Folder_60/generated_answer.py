def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i in range(12, 78) and s[i] >= ':' and (s[i] <= 'L'):
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result