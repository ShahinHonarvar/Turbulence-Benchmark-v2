def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i < 18 or i > 81 or (s[i] < 'W' or s[i] > '['):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)