def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if i < 19 or i > 32 or ord('f') > ord(s[i]) or (ord(s[i]) > ord('o')):
            filtered_s += s[i]
    return filtered_s