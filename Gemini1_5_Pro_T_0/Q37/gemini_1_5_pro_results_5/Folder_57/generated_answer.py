def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (27 <= i <= 85 and '!' <= s[i] <= 'B'):
            filtered_string += s[i]
    return filtered_string