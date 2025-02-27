def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (13 <= i <= 28 and 'c' <= s[i] <= 'n'):
            filtered_string += s[i]
    return filtered_string