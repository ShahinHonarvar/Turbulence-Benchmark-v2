def filter_chars(s):
    filtered_str = ''
    for i in range(len(s)):
        if i >= 43 and i <= 80 and (s[i] >= '=') and (s[i] <= 'E'):
            continue
        filtered_str += s[i]
    return filtered_str