def filter_chars(s):
    filtered_str = ''
    for i in range(len(s)):
        if i >= 10 and i <= 15 and (s[i] > 't') and (s[i] < 'v'):
            continue
        filtered_str += s[i]
    return filtered_str