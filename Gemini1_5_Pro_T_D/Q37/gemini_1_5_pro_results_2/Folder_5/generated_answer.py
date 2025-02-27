def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (24 <= i <= 82 and '5' <= s[i] <= '<'):
            filtered_string += s[i]
    return filtered_string