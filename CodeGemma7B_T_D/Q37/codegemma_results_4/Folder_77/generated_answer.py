def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 384 and i <= 411 and (s[i] >= '/') and (s[i] <= '8'):
            filtered_string += ''
        else:
            filtered_string += s[i]
    return filtered_string