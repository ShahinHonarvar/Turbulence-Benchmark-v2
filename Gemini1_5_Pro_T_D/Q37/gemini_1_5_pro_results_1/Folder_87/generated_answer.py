def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i >= 18 and i <= 81 and (s[i] >= 'W') and (s[i] <= '['):
            continue
        filtered_chars += s[i]
    return filtered_chars