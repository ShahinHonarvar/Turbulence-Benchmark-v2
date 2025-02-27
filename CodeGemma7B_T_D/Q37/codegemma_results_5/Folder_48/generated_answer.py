def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 513 and i <= 877 and (s[i] >= '?') and (s[i] <= 'n'):
            continue
        else:
            filtered_string += s[i]
    return filtered_string