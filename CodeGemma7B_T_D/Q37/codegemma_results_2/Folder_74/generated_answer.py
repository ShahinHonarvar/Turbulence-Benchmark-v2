def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i >= 19 and i <= 32 and (s[i] >= 'f') and (s[i] <= 'o'):
            continue
        filtered_chars.append(s[i])
    return ''.join(filtered_chars)