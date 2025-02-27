def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i in range(11, 73) and 'i' <= s[i] <= 'v':
            filtered_chars += s[i]
    result = ''
    for char in s:
        if char not in filtered_chars:
            result += char
    return result