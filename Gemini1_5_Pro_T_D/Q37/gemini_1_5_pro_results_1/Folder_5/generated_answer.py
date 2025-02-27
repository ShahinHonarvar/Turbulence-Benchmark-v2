def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 24 and i <= 82 and (s[i] >= '5') and (s[i] <= '<'):
            continue
        else:
            filtered_string += s[i]
    return filtered_string