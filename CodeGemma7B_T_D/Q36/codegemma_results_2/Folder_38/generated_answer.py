def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if i not in range(44, 48):
            filtered_s += s[i]
    for i in range(len(filtered_s)):
        if filtered_s[i] > '+' and filtered_s[i] < 'l':
            filtered_s = filtered_s[:i] + filtered_s[i + 1:]
    return filtered_s