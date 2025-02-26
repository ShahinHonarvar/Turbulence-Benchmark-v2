def filter_chars(s):
    result = s
    for i in range(672, 709):
        if 'X' < s[i] < '}':
            result = result.replace(s[i], '')
    return result