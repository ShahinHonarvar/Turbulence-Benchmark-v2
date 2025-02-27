def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if 31 < i < 73 and 'M' < s[i] < 'j':
            filtered_s += s[i] if s[i] not in filtered_s else ''
        else:
            filtered_s += s[i]
    return filtered_s