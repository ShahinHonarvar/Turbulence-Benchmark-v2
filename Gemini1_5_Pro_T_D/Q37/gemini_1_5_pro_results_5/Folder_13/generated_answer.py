def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        char = s[i]
        if not (124 <= i <= 854 and '9' <= char <= 's'):
            filtered_string += char
    return filtered_string