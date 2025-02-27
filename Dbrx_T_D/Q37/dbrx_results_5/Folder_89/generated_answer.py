def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i < 11 or i > 32 or (s[i] < '!' or s[i] > '@'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)