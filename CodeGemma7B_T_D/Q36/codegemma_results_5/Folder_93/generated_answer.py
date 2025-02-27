def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i > 51 and i < 88 and (s[i] > '&') and (s[i] < 'c'):
            continue
        filtered_chars.append(s[i])
    return ''.join(filtered_chars)