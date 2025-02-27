def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (15 <= i <= 55 and 'W' <= s[i] <= '{'):
            filtered_string += s[i]
    return filtered_string