def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 19 and i <= 22 and (']' <= s[i] <= 't'):
            filtered_string += s[i].replace(s[i], '')
        else:
            filtered_string += s[i]
    return filtered_string