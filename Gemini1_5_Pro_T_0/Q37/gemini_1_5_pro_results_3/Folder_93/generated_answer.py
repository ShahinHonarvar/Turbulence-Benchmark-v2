def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if not (38 <= i <= 69 and 'H' <= s[i] <= 'e'):
            filtered_string += s[i]
    return filtered_string