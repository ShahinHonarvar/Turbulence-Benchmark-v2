def filter_chars(s):
    t = 't'
    v = 'v'
    filtered_string = ''
    for i in range(len(s)):
        if i < 10 or i >= 15:
            filtered_string += s[i]
        elif s[i] > t and s[i] < v:
            pass
        else:
            filtered_string += s[i]
    return filtered_string