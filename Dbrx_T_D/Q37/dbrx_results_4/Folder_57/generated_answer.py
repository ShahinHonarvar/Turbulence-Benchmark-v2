def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i < 27 or i > 85 or (s[i] < '!' or s[i] > 'B'):
            filtered_chars += s[i]
    return filtered_chars