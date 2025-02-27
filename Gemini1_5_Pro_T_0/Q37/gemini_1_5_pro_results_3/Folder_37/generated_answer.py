def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (17 <= i <= 63 and 'O' <= s[i] <= '^'):
            filtered_string += s[i]
    return filtered_string