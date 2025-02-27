def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 24 <= i <= 82 and '5' <= s[i] <= '<':
            filtered_chars += s[i]
    result = ''
    for char in s:
        if char not in filtered_chars:
            result += char
    return result