def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 23 <= i <= 89 and 'w' <= s[i] <= '{':
            filtered_chars += s[i]
    result = ''
    for char in s:
        if char not in filtered_chars:
            result += char
    return result