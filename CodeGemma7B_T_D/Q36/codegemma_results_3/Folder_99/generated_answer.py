def filter_chars(s):
    filtered_s = s
    for i in range(476, 948):
        char = s[i]
        if char > 'b' and char < 'd':
            filtered_s = filtered_s.replace(char, '')
    return filtered_s