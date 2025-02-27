def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 25 and i <= 97 and (s[i] >= 'm') and (s[i] <= 'w'):
            continue
        else:
            filtered_string += s[i]
    return filtered_string