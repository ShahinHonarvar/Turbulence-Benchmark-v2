def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i in range(19, 93) and '8' <= s[i] <= 'm':
            continue
        else:
            filtered_string += s[i]
    return filtered_string