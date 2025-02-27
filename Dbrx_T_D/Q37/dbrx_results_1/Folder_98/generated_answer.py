def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if i < 8 or i > 9 or (s[i] < 'R' or s[i] > 't'):
            filtered_s += s[i]
    return filtered_s