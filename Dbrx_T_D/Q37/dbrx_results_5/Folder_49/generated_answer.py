def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if 42 <= ord(s[i]) <= 98 and 42 <= i <= 97:
            continue
        filtered_s += s[i]
    return filtered_s