def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (28 <= i <= 65 and 'O' <= s[i] <= 'd'):
            filtered_string += s[i]
    return filtered_string