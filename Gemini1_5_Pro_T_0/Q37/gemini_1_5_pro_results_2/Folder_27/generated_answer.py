def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 43 <= i <= 80 and '=' <= s[i] <= 'E':
            filtered_chars += s[i]
    result = ''
    for i in range(len(s)):
        if s[i] not in filtered_chars:
            result += s[i]
    return result