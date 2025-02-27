def filter_chars(s):
    filtered_str = ''
    for i in range(len(s)):
        if i >= 2 and i <= 6 and (s[i] >= '?') and (s[i] <= 'f'):
            continue
        filtered_str += s[i]
    return filtered_str