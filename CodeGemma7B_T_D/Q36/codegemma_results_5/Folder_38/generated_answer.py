def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i not in range(44, 48):
            filtered_string += s[i]
    return filtered_string