def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 22 <= i <= 85 and '7' <= s[i] <= 'e':
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result