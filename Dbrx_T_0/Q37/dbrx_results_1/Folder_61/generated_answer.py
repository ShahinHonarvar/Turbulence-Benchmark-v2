def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i < 5 or i > 6 or (s[i] < 'G' or s[i] > 'p'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)