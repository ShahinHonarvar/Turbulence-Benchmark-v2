def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        char = s[i]
        if not (12 <= i <= 88 and '&' <= char <= 'v' and (char in s[12:89])):
            filtered_string += char
    return filtered_string