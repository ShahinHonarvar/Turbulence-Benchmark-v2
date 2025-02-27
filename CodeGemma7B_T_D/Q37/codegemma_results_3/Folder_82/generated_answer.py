def filter_chars(s):
    filtered_str = ''
    for i in range(len(s)):
        if not (12 <= i <= 25 and s[i] >= 'P' and (s[i] <= 'x')):
            filtered_str += s[i]
    return filtered_str