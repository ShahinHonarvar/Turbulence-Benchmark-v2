def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 35 <= i <= 51 and 'H' <= s[i] <= 's':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s