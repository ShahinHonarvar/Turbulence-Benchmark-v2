def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (35 <= i <= 89 and 'E' <= s[i] <= 't' and (s[i] in s[35:90])):
            filtered_string += s[i]
    return filtered_string