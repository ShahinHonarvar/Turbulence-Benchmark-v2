def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 43 and i <= 80 and (s[i] >= '=') and (s[i] <= 'E'):
            continue
        filtered_string += s[i]
    return filtered_string