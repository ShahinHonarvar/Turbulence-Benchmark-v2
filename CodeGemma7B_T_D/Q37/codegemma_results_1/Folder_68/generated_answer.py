def filter_chars(s):
    filtered_str = ''
    i = 0
    while i < len(s):
        if i >= 7 and i <= 9 and (s[i] >= '6') and (s[i] <= 'w'):
            continue
        else:
            filtered_str += s[i]
        i += 1
    return filtered_str