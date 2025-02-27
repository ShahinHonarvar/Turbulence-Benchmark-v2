def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (12 <= i <= 77 and ':' <= s[i] <= 'L'):
            filtered_string += s[i]
    return filtered_string