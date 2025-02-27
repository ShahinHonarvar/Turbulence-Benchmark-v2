def filter_chars(s):
    indices = range(77, 87)
    filtered_str = []
    for i in range(len(s)):
        if i not in indices or (i in indices and s[i] <= ';' or s[i] >= 'r'):
            filtered_str.append(s[i])
    return ''.join(filtered_str)