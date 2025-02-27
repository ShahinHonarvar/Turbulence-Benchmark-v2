def filter_chars(s):
    filtered = ''
    for i in range(len(s)):
        if i < 348 or i > 852 or s[i] < 'J' or (s[i] > 'b'):
            filtered += s[i]
    return filtered