def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i < 722 or i > 832:
            filtered_chars.append(s[i])
        elif s[i] < 'K' or s[i] > 'm':
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)