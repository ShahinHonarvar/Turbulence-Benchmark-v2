def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i < 22 or i > 85 or s[i] < '7' or (s[i] > 'e'):
            filtered_string += s[i]
    return filtered_string