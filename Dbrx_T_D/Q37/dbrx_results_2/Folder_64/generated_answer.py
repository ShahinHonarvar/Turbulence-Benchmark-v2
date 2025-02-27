def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if (i < 1 or i > 7) and (s[i] < 'L' or s[i] > 'a'):
            filtered_s += s[i]
    return filtered_s