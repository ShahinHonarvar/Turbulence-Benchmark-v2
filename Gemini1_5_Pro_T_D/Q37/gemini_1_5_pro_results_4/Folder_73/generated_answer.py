def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 22 and i <= 85 and (s[i] >= '7') and (s[i] <= 'e'):
            continue
        filtered_string += s[i]
    return filtered_string