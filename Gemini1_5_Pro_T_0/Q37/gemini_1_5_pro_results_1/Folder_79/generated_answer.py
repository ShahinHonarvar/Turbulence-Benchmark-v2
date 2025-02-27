def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 10 <= i <= 52 and '@' <= s[i] <= 'T' and (s[i] not in filtered_chars):
            filtered_chars += s[i]
    result = ''
    for char in s:
        if char not in filtered_chars:
            result += char
    return result