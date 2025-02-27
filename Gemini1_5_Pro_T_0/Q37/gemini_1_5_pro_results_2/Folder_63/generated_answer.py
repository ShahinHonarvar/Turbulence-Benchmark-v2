def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 42 <= i <= 92 and '/' <= s[i] <= 'a':
            if s[i] not in filtered_chars:
                filtered_chars += s[i]
    result = ''
    for char in s:
        if char in filtered_chars:
            continue
        result += char
    return result