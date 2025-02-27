def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if not 52 <= i <= 81 or (s[i] < 'A' or s[i] > 'U'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)