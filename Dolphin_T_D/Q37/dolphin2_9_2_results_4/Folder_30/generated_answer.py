def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if i < 41 or i > 64 or (s[i] < 'K' or s[i] > ']'):
            filtered_s += s[i]
    return filtered_s