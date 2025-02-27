def filter_chars(s):
    filtered_str = ''
    for i in range(len(s)):
        if not (27 <= i <= 85 and '!' <= s[i] <= 'B'):
            filtered_str += s[i]
    return filtered_str