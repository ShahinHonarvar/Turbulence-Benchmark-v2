def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        char = s[i]
        if not (29 <= i <= 97 and '-' <= char <= 'n'):
            filtered_string += char
    return filtered_string