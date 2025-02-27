def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if not (11 <= i <= 32 and '!' <= s[i] <= '@'):
            filtered_chars += s[i]
    return filtered_chars