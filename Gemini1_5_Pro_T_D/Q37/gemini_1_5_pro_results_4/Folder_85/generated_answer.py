def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 28 and i <= 65 and (s[i] >= 'O') and (s[i] <= 'd'):
            if s[i] not in filtered_string:
                filtered_string += s[i]
        else:
            filtered_string += s[i]
    return filtered_string