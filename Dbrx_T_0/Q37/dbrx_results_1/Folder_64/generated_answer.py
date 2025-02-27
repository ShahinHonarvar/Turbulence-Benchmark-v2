def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i < 1 or i > 7 or (s[i] < 'L' or s[i] > 'a'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)