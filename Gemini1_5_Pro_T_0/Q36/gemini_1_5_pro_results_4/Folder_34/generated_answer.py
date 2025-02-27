def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if 10 <= i <= 79:
            if not '?' < s[i] < 'm':
                filtered_string += s[i]
        else:
            filtered_string += s[i]
    return filtered_string