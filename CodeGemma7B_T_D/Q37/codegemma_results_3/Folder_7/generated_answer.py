def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if i >= 521 and i <= 722 and (s[i] >= '>') and (s[i] <= '_'):
            continue
        else:
            filtered_s += s[i]
    return filtered_s