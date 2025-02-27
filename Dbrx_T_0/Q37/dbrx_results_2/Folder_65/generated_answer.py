def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i < 61 or i > 70:
            filtered_chars.append(s[i])
        elif s[i] < '0' or s[i] > '@':
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)