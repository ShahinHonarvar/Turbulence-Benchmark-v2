def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i in range(12, 89):
            if not '&' <= s[i] <= 'v':
                filtered_string += s[i]
        else:
            filtered_string += s[i]
    return filtered_string