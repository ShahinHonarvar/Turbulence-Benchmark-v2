def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i in range(20, 63) and 'i' <= s[i] <= 'k':
            continue
        else:
            filtered_chars += s[i]
    return filtered_chars