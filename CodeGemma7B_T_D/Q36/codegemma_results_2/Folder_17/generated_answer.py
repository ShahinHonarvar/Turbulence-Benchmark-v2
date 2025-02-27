def filter_chars(s):
    filtered_str = ''
    for i in range(len(s)):
        if s[i] > 'K' and s[i] < 'a' and (i not in range(18, 95)):
            filtered_str += s[i]
    return filtered_str