def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (11 <= i <= 72 and 'i' <= s[i] <= 'v'):
            filtered_string += s[i]
    return filtered_string